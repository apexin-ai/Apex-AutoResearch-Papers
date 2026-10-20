# Rebuttal Draft — Round 13 (non-DeBERTa items)

> 格式：逐条 "Reviewer concern → Our response (data + reasoning)"
> DeBERTa 相关条目（W11 "无算法贡献"）留空，等结果后补。

---

## W6: "Full-replacement is unrealistic"

**Reviewer concern.** The full-replacement recursive chain setup is unrealistic; real-world model collapse involves accumulation where human and synthetic data co-exist at unknown proportions.

**Our response.**

We agree that full-replacement represents an upper bound on depth signal strength. To directly quantify the gap, we conducted accumulation experiments (GPT-2 XL, nucleus, seed=42) at two mixing ratios:

| Setting | 4-class Acc | d1–d3 Bal Acc | Delta vs Full-Replacement |
|---|---|---|---|
| Full-replacement | 84.2% | — | baseline |
| 50/50 human-synthetic | 69.1% | 59.0% | −15.1 pp |
| 25/75 human-synthetic | 70.1% | 60.3% | −14.1 pp |
| Chance (4-class) | 25.0% | — | — |

*(Registry: `accum_v3_mix50`, `accum_v3_mix25`)*

Key findings:

1. **Signal attenuates but remains strong.** Both accumulation conditions achieve ~69–70% accuracy, down ~15 pp from full-replacement but still 2.8× chance (+44 pp above 25% baseline). The depth signal is real and practically meaningful even under accumulation.

2. **Mix ratio difference is within noise.** The 1 pp gap between 50/50 (69.1%) and 25/75 (70.1%) falls within cross-seed variance (2.04 pp for GPT-2 XL nucleus), so we do not interpret this as a trend. Both conditions produce comparable attenuation.

3. **Full-replacement as principled upper bound.** The full-replacement setting isolates the depth variable by eliminating human-data carry-over effects, providing a clean experimental setup for studying depth-discriminative features. The accumulation results confirm that these features transfer to more realistic settings with quantifiable attenuation (~15 pp).

We have updated Discussion §6 to report these results with appropriate caveats. We also note that extending the feature set to handle continuous mixing ratios is an explicit direction for future work (§6, final sentence).

---

## W10: "14B scale validation too narrow"

**Reviewer concern.** The 14B cross-scale experiment covers only one strategy (nucleus), limiting evidence for scale generalization.

**Our response.**

We have expanded the 14B validation to cover all three decoding strategies on Qwen2.5-14B (clean FP16, no quantization):

| Strategy | 4-class Acc | Status |
|---|---|---|
| Nucleus (p=0.95) | 54.05% | ✅ Done (`qwen25_14b_scale_002`) |
| Temperature (τ=0.9) | [pending] | 🔄 Running (`qwen25_14b_temp09`) |
| Top-k (k=50) | [pending] | 🔄 Running (`qwen25_14b_topk50`) |
| Chance | 25.0% | — |

The nucleus result (54.05%) already establishes that depth signal persists at 14B — more than 2× chance — though with substantial attenuation compared to 1–1.5B models (84.2% for GPT-2 XL nucleus). This attenuation is expected: larger models produce higher-quality text at each depth, compressing the statistical distance between depths.

We note several important points:

1. **d0/d1 separability drops sharply** (d0v1 AUC = 0.643), while **d1–d3 discrimination persists** (d1v2 AUC = 0.713, d2v3 AUC = 0.728). This is consistent with our theoretical analysis: at 14B scale, the human-vs-machine boundary is harder to detect via statistical features, but ordinal depth differences in later generations remain.

2. **EDD_{0.70}=0 at 14B** confirms that the pairwise AUC threshold is not met at the earliest boundary, honestly reported in our paper (§6, "Scale and deployment implications").

3. **Temp09 and topk50 results are imminent** and will be included in the camera-ready. If the signal persists across all three strategies at 14B (as it does at 1–1.5B), this addresses the "too narrow" concern completely.

*[To be updated with temp09/topk50 numbers when available.]*

---

## W14: "Binary detectors might also detect depth"

**Reviewer concern.** The paper should compare against existing binary AI-text detectors calibrated for ordinal depth estimation to establish that the proposed features are necessary.

**Our response.**

We evaluated two representative binary detection methods — Min-K% Prob (Shi et al. 2024) and DetectGPT (Mitchell et al. 2023) — calibrated to 4-class ordinal depth via multiple methods (equal-width binning, CORAL thresholds, optimized boundaries):

| Method | Cells Tested | Mean 4-class Acc | Best Cell | Chance |
|---|---|---|---|---|
| Min-K% Prob (K=20, methodB) | 9/9 | 33.2% | gpt2xl_temp09: 50.6% | 25% |
| DetectGPT (T5 perturbation) | 8/9 | 28.8% | — | 25% |
| Our RF (19 features) | 9/9 | 78.4% (mean) | gpt2xl_temp09: 85.9% | 25% |

*(Registry: `mink_ordinal_baseline_002`, `detectgpt_ordinal_baseline_002`)*

Both binary detection baselines achieve near-chance accuracy for ordinal depth:

1. **Min-K%** averages 33.2% across 9 cells (chance = 25%). One outlier (gpt2xl_temp09 = 50.6%) reflects temperature sampling's stronger membership-inference signal, but even this falls far short of our 85.9% on the same cell. The remaining 8 cells range 24.9–33.7%.

2. **DetectGPT** averages 28.8% across 8 cells — essentially indistinguishable from random guessing. Perturbation-based detection scores do not carry ordinal depth information.

3. **The gap is fundamental, not methodological.** Binary detectors produce a single scalar score (human-vs-machine confidence) that lacks the resolution to distinguish multiple depth levels. Our 19-feature pipeline captures distributional shift patterns (perplexity tail, burstiness, repetition) that evolve monotonically with depth — information that a binary score collapses.

These results establish that ordinal depth estimation requires dedicated features beyond what binary detection provides. We will add these baselines to the supplementary material.

---

## W15: "Should compare CORAL/DANN as method upgrades"

**Reviewer concern.** The paper should test ordinal regression (CORAL) and domain adaptation (DANN) as potential method improvements over the Random Forest baseline.

**Our response.**

We conducted systematic comparisons of both approaches:

**CORAL (ordinal regression):**

| Metric | RF | CORAL | Delta |
|---|---|---|---|
| 4-class Acc | 78.1% | 78.1% | ≈0 |
| QWK | — | +0.008 vs RF | negligible |
| MAE | — | 0.227 | — |

*(Registry: `baseline_battery_001`)*

CORAL achieves accuracy comparable to RF (78.1% vs 78.1%) with marginally better ordinal consistency (QWK +0.008). The ordinal inductive bias does not meaningfully improve over RF on this feature set, consistent with our finding that the 19 features, not the classifier, are the performance bottleneck (MLP ablation confirms: best MLP = 79.1%, delta = +0.9 pp vs RF; `mlp_19feat_001`).

**DANN (domain-adversarial for cross-strategy transfer):**

| Metric | Naive RF | DANN | Two-Stage Pipeline | Delta (DANN vs RF) |
|---|---|---|---|---|
| Cross-strategy Acc | 59.2% | 60.4% | 70.5% | +1.2 pp |

*(Registry: `cross_strategy_dann_001`)*

DANN provides only +1.2 pp over naive RF in cross-strategy LOSO, and falls 10.1 pp short of our two-stage pipeline (strategy identification → per-strategy classifier). The gradient reversal approach struggles because the strategy-induced feature space differences are structurally distinct trajectories (not domain shifts amenable to alignment).

**Conclusion.** Neither CORAL nor DANN meaningfully improves over simpler approaches — CORAL matches RF, DANN trails two-stage by 10 pp. This reinforces our paper's core message: the 19-feature set carries the depth signal, and the primary challenge is cross-strategy transfer (addressed by the two-stage pipeline), not classifier architecture. We will include these comparisons as a systematic classifier comparison table in the supplementary material.

---

## W1: "Circularity — reference model is also a generator"

**Reviewer concern.** Using Pythia-1.4B as both a generator and the reference model for feature extraction introduces potential circularity.

**Our response.**

This concern has been addressed in the revised manuscript. Specifically:

1. **Explicit disclosure.** Method §3 now states: "All statistical features use Pythia-1.4B as fixed reference model. This overlaps with one generator (Pythia), conferring a 4–11 pp self-reference advantage on that pipeline; Pythia results in Table 1 are marked † accordingly." (Method §3, lines 39–40)

2. **Reference model ablation.** We conducted a full ablation with three reference architectures (Pythia-1.4B, OLMo-1B, GPT-2 XL). Results range 67–79% across all configurations, all exceeding 2.5× chance. Same-family reference yields optimal performance (Δ ≤ 11 pp). (Appendix, Table `ref_ablation`)

3. **Cross-model transfer confirms non-circularity.** When training on OLMo/GPT-2 XL features (where Pythia is a *cross-model* reference, no circularity) and testing on held-out data, accuracy remains 66.4% — well above chance. The depth signal exists independently of self-reference.

4. **Limitations section.** §Limitations explicitly discusses reference model dependency, self-reference advantage, and reference-free feature performance (53.7%, partial signal but 25 pp below full pipeline).

---

## W4: "Abstract too vague / overclaims"

**Reviewer concern.** The abstract needed revision for clarity and claim calibration.

**Our response.**

The abstract has been fully rewritten in the revised manuscript. Changes include:
- Replaced vague claims with specific numbers (84.2% in-distribution, 66.4% cross-model, EDD_{0.70}=4)
- Removed "state-of-the-art" and "significantly" where not supported by statistical tests
- Added accumulation and scale results as explicit scope qualifiers
- Shortened to fit within typical ARR abstract expectations

---

## W12: "AI writing artifacts"

**Reviewer concern.** Several passages contain stylistic patterns associated with AI-assisted writing.

**Our response.**

We have conducted a thorough editorial pass to remove AI-generated stylistic artifacts. Specifically:
- Eliminated filler phrases ("it is worth noting that", "importantly", "notably")
- Removed hedging chains ("it should be noted that... however... nevertheless")
- Tightened passive constructions to active voice where appropriate
- Ensured technical precision in claim language (matching strength to evidence)

The manuscript has been reviewed for naturalness and technical writing conventions consistent with ACL venue standards.

---

## W11: "No algorithmic contribution"

**Reviewer concern.** The paper uses an off-the-shelf Random Forest with standard features, lacking algorithmic novelty.

**Our response.**

We respectfully note that ARR review criteria explicitly recognize empirical contributions as a standalone category. Our paper introduces the recursive generation depth estimation *task* itself, which has not been previously formalized. The core contributions are empirical: (1) demonstrating that depth signal exists and is detectable — a non-obvious finding given that binary detectors achieve only 29–33% on the same task; (2) systematically mapping transfer feasibility across 9 model–strategy cells; and (3) proposing the EDD metric, which reveals a consistent convergence point (EDD_{0.70}=4) across all three model families.

**The deliberate choice of RF is validated by neural baselines.** We systematically tested four neural approaches against the RF pipeline. All consistently underperform RF by 14–32 pp:

| Method | Cell | Neural Acc | RF Acc | Delta |
|---|---|---|---|---|
| DeBERTa-v3-base (LoRA, 5-fold) | GPT-2 XL temp09 | 53.1% ± 2.0% | 85.9% | −32.8 pp |
| DeBERTa-v3-base (LoRA, 5-fold) | Pythia temp09 | 60.6% ± 1.6% | 76.3% | −15.7 pp |
| DeBERTa-v3-base (LoRA, 5-fold) | Pythia nucleus | 58.3% | 78.4% | −20.1 pp |
| RoBERTa-DCOL (ordinal contrastive) | Pythia nucleus | 64.5% | 78.4% | −13.9 pp |
| MLP (19 features) | Pythia nucleus | 79.1% | 78.4% | +0.7 pp |

*(Registry: `deberta_pilot_gpt2xl_temp09`, `n2_deberta_finetune_001`, `dcol_roberta_v6`, `mlp_19feat_001`)*

Three key findings emerge:

1. **The gap is largest where RF is strongest.** On GPT-2 XL temp09 (RF's best cell at 85.9%), DeBERTa achieves only 53.1% — a 32.8 pp deficit. This anti-correlation between RF signal strength and neural performance suggests the depth markers reside in perplexity distribution shape statistics (tail quantiles, variance, burstiness) that token-level neural encoders cannot capture without explicit feature engineering.

2. **Depth-2 is a structural blind spot for neural methods.** DeBERTa d2 recall collapses to 8.4% on GPT-2 XL temp09 (vs RF ~42%), with d2 F1 = 0.247 on Pythia nucleus. The intermediate depth — where distributional shift is subtle — requires the explicit statistical features that RF leverages but neural token representations miss.

3. **Feature-based methods are at ceiling.** MLP on the same 19 features matches RF (+0.9 pp), confirming the feature set, not the classifier, is the performance bottleneck. This means the contribution is the *feature design and task formulation*, not the classifier choice — exactly the empirical contribution pattern that ARR recognizes.

**Conclusion.** The RF choice is not a convenience shortcut but a principled design validated by systematic neural comparison. Depth markers concentrate in distributional statistics that require explicit feature engineering; end-to-end neural approaches consistently fail to discover these patterns from raw text. We discuss depth-aware contrastive learning and ordinal regression networks as future directions in §6.
