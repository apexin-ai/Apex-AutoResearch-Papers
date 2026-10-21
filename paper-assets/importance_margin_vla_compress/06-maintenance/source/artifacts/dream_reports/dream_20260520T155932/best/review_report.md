---
dream_id: dream_20260520T155932
tier: best
overall_score: borderline accept (6/10)
timestamp: 2026-05-20T16:42:49.010878+00:00
---

# Dream Review Report: "Why Token Pruning Crashes Some Robot Policies but Not Others"

**Venue:** CoRL 2026 | **Review Mode:** Full (2-Reviewer Roundtable) | **Date:** 2026-05-20

---

## Roundtable Process

- **R1** — Methods & Experiments focus
- **R2** — Novelty, Significance & Related Work focus
- **Step 1:** Independent reviews → **Step 2:** Cross-sharing → **Step 3:** Convergence → **Step 4:** This consolidated report

---

## 1. Summary

The paper presents the first systematic cross-architecture study of visual token pruning robustness across 6 VLA models spanning 4 connector families. It discovers that the effective vision-to-LLM projection pipeline — not model size — determines pruning tolerance along a continuous spectrum. A four-class taxonomy is proposed (immune → gentle graded → threshold-graded → smooth graded → catastrophic), with Importance CV as a zero-cost predictor. A Diagnose-then-Compress framework pairs this diagnostic with Vision Token Re-encoding (VTR), a ~22M parameter cross-attention module that recovers pixel-shuffle from 0% to 60.1% SR and achieves 45–58% SR on MLP projectors at 75–87.5% compression.

---

## 2. Strengths (Consensus)

- **Well-designed cross-architecture comparison.** Testing 6 models × 4 connector families with controlled variables (π0 vs OpenVLA: same token count, same SigLIP encoder, different connector) is the paper's strongest contribution. No prior work has systematically isolated the connector's role in determining pruning robustness.

- **SmolVLA cliff-edge finding is thoroughly established.** The demonstration that removing just 5% of tokens from a pixel-shuffle connector yields 0% SR is surprising and important. Verified across all pruning strategies (random, ACIS, ToMe, geometric priors), multiple task suites (Object, Spatial, Goal), and official checkpoints. This negative result alone is a service to the community.

- **VTR mechanism isolation is rigorous on SmolVLA.** Three-pronged evidence: (1) M=128 passthrough control (+13.2pp above baseline → re-encoding is causal, not compression), (2) architecture independence (MLP adapter ≈ cross-attention, p=0.15), (3) flat M-curve (all 5 M values within ±5pp → compression ratio doesn't matter for pixel-shuffle). The 3-seed protocol with mean±std reporting adds credibility.

- **Actionable practitioner guidance.** The CV diagnostic (single forward pass, zero cost) is immediately usable by engineers deploying VLAs. The threshold table (CV < 0.05 = safe to prune, CV > 0.25 = VTR required) provides concrete decision criteria.

- **Honest reporting of negative results.** Full VTR on OpenVLA M=128 producing 0% SR (overfitting) is acknowledged and reframed as connector-dependency. The OFT eval bug is disclosed. This builds credibility.

- **Pruning method equivalence analysis (Table 8).** L2-norm vs random producing equivalent results on OpenVLA (max |Δ|=2.0pp across all k) directly addresses a cross-model methodology concern and strengthens the architecture-dependency claim.

- **Sound statistical framework.** Wilson 95% CIs, 500 episodes per configuration, Welch's t-tests for pairwise comparisons, 3-seed replication for VTR M-sweep.

---

## 3. Weaknesses (Consensus)

### 3.1 CV Predictor Overclaimed (Both R1 and R2)

The paper claims CV is a "continuous predictor" validated on **exactly 5 data points** (π0=0.038, RoboFlamingo=0.11, X-VLA=0.151, OpenVLA=0.215, SmolVLA=0.314). With 5 points, any monotonic function appears predictive. The proposed thresholds (CV<0.05, 0.05–0.15, 0.15–0.25, >0.25) are post-hoc bin boundaries drawn around individual data points, not validated decision boundaries. The paper should reframe this as an "empirical trend observed across 5 architectures" rather than a validated continuous predictor. Leave-one-out validation or prediction on a held-out architecture would strengthen this claim substantially.

### 3.2 Heterogeneous Evaluation Modes (R1, endorsed by R2)

The taxonomy's left anchor (π0 = "immune") rests entirely on offline normalized L1 loss, not closed-loop SR. Offline loss is known to correlate poorly with closed-loop manipulation success (cf. diffusion policy literature). OpenVLA-OFT contributes only entropy data due to a confirmed eval bug (k=1.0 = 0% SR). Only 4 of 6 models share a common evaluation metric. This is a significant methodological limitation for a paper whose central claim is a unified taxonomy.

### 3.3 Thin Seed Robustness (R1, endorsed by R2)

Only 2 seeds for 4 selected configurations. The X-VLA k=0.7 cliff shows 4.2pp variance across 2 seeds (56.2% vs 52.0%). The OpenVLA main pruning curve (Table 3) appears single-seed. For a paper where the shape of degradation curves is the core contribution, broader seed replication (≥3 seeds for all main curves) is needed.

### 3.4 VTR "Universal" Claim Overstated (Both R1 and R2)

VTR is tested on exactly 2 of 4 connector types (pixel-shuffle and MLP). Not tested on linear projection (π0) or Perceiver Resampler (RoboFlamingo). The claim should be restricted to "applicable across pixel-shuffle and MLP connectors." Additionally, OpenVLA VTC-only results (Table 7) lack multi-seed replication (no ±std), contrasting with SmolVLA's 3-seed protocol.

### 3.5 Inadequate Related Work (R2, endorsed by R1)

**Only 10 references** — far below the expected 25–40 for a CoRL submission. Critical omissions include:
- **Connector architecture lineage:** Perceiver/Perceiver IO (Jaegle et al. 2021/2022), BLIP-2/Q-Former (Li et al. 2023), Flamingo (Alayrac et al. 2022) — all directly relevant to VTR's architectural ancestry
- **ViT token efficiency:** DynamicViT (Rao et al. 2021), EViT (Liang et al. 2022), LLaVA-PruMerge (Shang et al. 2024)
- **VLA efficiency:** VLA-IAP, VLA-Cache, EfficientVLA, VLA-Pruner — concurrent works mentioned but not cited
- **Foundational:** LLaVA (Liu et al. 2023), Octo (Ghosh et al. 2024), pixel-shuffle origin (Shi et al. 2016), DINOv2, Open X-Embodiment
- **VTR = Q-Former/Perceiver Resampler:** The paper does not discuss VTR's architectural identity with established cross-attention compression modules. This is a significant positioning gap.

### 3.6 LIBERO-Only Evaluation (R2, endorsed by R1)

Single simulation benchmark, no real-robot experiments. CoRL reviewers typically expect either real-robot results or multi-benchmark evaluation (e.g., LIBERO + CALVIN + SimplerEnv). The SmolVLA cliff-edge and VTR recovery findings would be substantially stronger with at least one additional benchmark.

### 3.7 RoboFlamingo Data Quality (Both R1 and R2)

The 42% baseline SR is low, compressing the observable degradation range. Table 5 lacks confidence intervals and seed information. The CV=0.11 data point is critical for the continuous spectrum but rests on the weakest experimental foundation. The relationship between low baseline and pruning tolerance is not disentangled — is RoboFlamingo "gentle graded" because of the Perceiver Resampler, or because the model is already performing near chance on some tasks?

---

## 4. Key Questions for Authors

1. **π0 closed-loop validation:** Can you provide closed-loop evaluation on even 2–3 LIBERO tasks at k=0.5? The "immune" anchor of the entire taxonomy depends on offline-only evidence.

2. **CV predictor validation:** With 5 data points and 4 bins, how do you distinguish a continuous relationship from 5 discrete categories? Have you considered leave-one-out prediction (e.g., predicting X-VLA from the other 4)?

3. **OpenVLA VTC-only seeds:** Are the Table 7 results (45%, 52%, 58%) single-seed? Why the asymmetric reporting standard vs. SmolVLA's 3-seed protocol?

4. **VTR vs Q-Former:** VTR is architecturally identical to Q-Former/Perceiver Resampler. How do you position VTR relative to these established methods? Is the contribution the module itself or the diagnostic-guided application?

5. **X-VLA seed variance:** The cliff at k=0.7 shows 4.2pp variance across 2 seeds. With more seeds, could the cliff characterization change? What is the per-task SR distribution at the cliff point?

6. **VTR vs parameter-free methods on OpenVLA:** Why was ToMe not tested as a VTR alternative on OpenVLA? ToMe is parameter-free; its inclusion would justify VTR's 22M parameter cost.

7. **RoboFlamingo baseline reliability:** Is 42% representative of the Perceiver Resampler's true capability, or is it limited by training issues? How does this affect the "gentle graded" classification?

8. **Concurrent works comparison:** For published concurrent works (LightVLA ICRA 2026, See What Matters ICML 2026), could you reproduce their methods on SmolVLA to demonstrate predicted failure? This would be a powerful validation of the diagnostic framework.

---

## 5. Experiment Coverage Assessment

Comparing against the full experimental design (review_context.yaml):

| Experiment | Status | Quality |
|---|---|---|
| OpenVLA VTC-only M=32/64/96 | ✅ Covered | Single-seed (no CI) |
| OpenVLA L2-norm pruning k=0.95/0.9/0.7/0.5/0.3 | ✅ Covered | Adequate (Table 8) |
| X-VLA seed44 k=0.7/0.9 | ✅ Covered | Adequate (Table 9) |
| OpenVLA seed43 k=0.7/0.5 | ✅ Covered | Adequate (Table 9) |
| RoboFlamingo baseline + pruning | ✅ Covered | Below standard (no CI, no seeds) |

**Coverage:** 12/12 imagined experiments reflected in the paper. The primary gap is not missing experiments but inconsistent rigor across models — SmolVLA VTR has 3-seed replication while OpenVLA VTC and RoboFlamingo have single-seed or unreported seed protocols.

---

## 6. Scores

### Dimension Scores (CoRL 1–10 scale)

| Dimension | Score | Justification |
|---|---|---|
| **Novelty** | 5 | Cross-architecture study design is genuinely novel; CV diagnostic is useful but straightforward; VTR is architecturally identical to Q-Former (not novel as a method); taxonomy is descriptive rather than theoretical. Primary novelty is empirical. |
| **Significance** | 6 | Addresses real deployment concern; CV diagnostic is actionable; SmolVLA cliff-edge is an important warning. Limited by LIBERO-only eval, no real-robot results, and observation that linear VLAs already don't need pruning while pixel-shuffle VLAs need VTR (adding complexity). |
| **Methods** | 6 | Core comparison framework is sound; statistical reporting is appropriate; true removal protocol is well-justified. Weakened by heterogeneous eval modes (offline vs closed-loop), thin seed analysis, and incomplete VTR coverage across connector types. |
| **Experiments** | 6 | Broad coverage (6 models, multiple methods, VTR M-sweep). SmolVLA ablation is excellent. Weakened by: π0 offline-only, RoboFlamingo low quality, OpenVLA VTC single-seed, OFT contributing no pruning data, and emerging seed variance concerns at X-VLA cliff. |
| **Related Work** | 4 | 10 references is critically insufficient. Missing foundational citations (Perceiver, Q-Former, Flamingo, LLaVA, DynamicViT). VTR's relationship to Q-Former not discussed. Concurrent works listed but not compared. |
| **Writing/Presentation** | 7 | Clear narrative structure (diagnosis → taxonomy → method). Tables are well-organized. Claims are mostly well-calibrated except "universal" and "continuous predictor." Title delivers on its promise. |

### Overall Score: 5.5 → **6 (Marginally above acceptance threshold)**

### Confidence: 4/5

---

## 7. Consolidated Assessment

**The paper addresses an important and timely question with a well-designed empirical study.** The core finding — that the vision connector, not model size, determines token pruning robustness — is sound, useful, and well-evidenced for at least 3 of the 6 models (SmolVLA, OpenVLA, X-VLA). The SmolVLA cliff-edge finding alone is a service to the community.

**However, three addressable issues hold the paper at the borderline:**

1. **Related work must at least double in size.** The 10-reference bibliography is the most glaring weakness. VTR's relationship to Q-Former/Perceiver needs explicit discussion. Concurrent VLA efficiency works need proper citation and positioning.

2. **Claims need calibration.** "Continuous predictor" → "empirical trend across 5 architectures." "Universal compression" → "applicable to pixel-shuffle and MLP connectors." These are not minor wording changes — they affect the reader's assessment of contribution magnitude.

3. **Evaluation consistency.** The heterogeneous eval modes (offline π0, broken OFT, low-baseline RoboFlamingo) mean the 6-model taxonomy is really a 3-model taxonomy (SmolVLA, OpenVLA, X-VLA) with 3 supplementary data points of varying quality. Either strengthen the supplementary evidence (closed-loop π0, fixed OFT, better RoboFlamingo baseline) or be transparent that the core taxonomy rests on 3 models.

**With these addressed, the paper would be a solid accept at CoRL.** The empirical contribution is real and the diagnostic framework is useful. In its current form, it is a borderline paper that could go either way depending on reviewer tolerance for incomplete evaluation and thin related work.

---

## 8. Actionable Revision Priorities

1. **[High] Expand references to 25+.** Add Q-Former, Perceiver, Flamingo, LLaVA, DynamicViT, EViT, Octo, pixel-shuffle origin, concurrent VLA works. Discuss VTR's architectural lineage explicitly.
2. **[High] Calibrate claims.** Reframe CV as empirical trend; restrict "universal" to tested connectors; qualify π0 "immune" with offline caveat.
3. **[High] Add multi-seed replication for OpenVLA VTC-only.** At minimum 3 seeds for M=32 and M=64 to match SmolVLA's reporting standard.
4. **[Medium] Add one additional benchmark or real-robot probe.** Even SimplerEnv on 1–2 models would help.
5. **[Medium] Strengthen RoboFlamingo.** Add CIs and seed info to Table 5; discuss baseline quality.
6. **[Low] Consider closed-loop π0 evaluation on a small subset.** Even 100 episodes at k=0.5 would strengthen the taxonomy's left anchor.
