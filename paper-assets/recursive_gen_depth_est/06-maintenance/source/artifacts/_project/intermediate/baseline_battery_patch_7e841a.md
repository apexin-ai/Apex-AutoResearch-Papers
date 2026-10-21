# Unified Baseline Battery Patch — DetectGPT + Min-K% + Binoculars (D048)

> 三合一 binary detector baseline 对比材料。用于论文 §5 Baseline Comparison 和 §6 Discussion。
> 待 14B 结果后与 scale robustness 一起统一 patch 论文。

## 1. Main Comparison Table (§5)

**Table: Binary Detection Methods as Ordinal Depth Baselines**

| Method | Paradigm | Calibration | 9-cell Mean Acc | vs Chance (+pp) | Source |
|--------|----------|-------------|-----------------|-----------------|--------|
| Random chance | — | — | 25.0% | — | — |
| DetectGPT | Perturbation discrepancy | Best of 3 | 28.8% | +3.8 | detectgpt_002+004 |
| Min-K% Prob | Membership inference | Best of 3 | 33.2% | +8.2 | mink_002 |
| DeBERTa-v3-base + LoRA | Neural (fine-tuned) | End-to-end | 53.1–60.6% | +28–36 | deberta_pilot (2-cell) |
| Binoculars (threshold) | Cross-perplexity | Equal-width | 69.8% | +44.8 | binoculars_001 |
| Binoculars (RF_single) | Cross-perplexity | RF on 1 feature | 63.7% | +38.7 | binoculars_001 |
| **Binoculars (RF_multi)** | **Cross-perplexity** | **RF on 11 features** | **78.1%** | **+53.1** | binoculars_001 |
| **Our 19-feature RF** | **Statistical features** | **RF on 19 features** | **78.4%** | **+53.4** | baseline_battery_001 |

Notes:
- All results 5-fold stratified CV, 200 trees for RF methods
- DetectGPT: T5-large perturbation, GPT-2 Large scoring, 5 perturbations/passage
- Binoculars: observer=pythia-1.4b, performer=pythia-410m
- DeBERTa: 2-cell pilot only (gpt2xl_temp09, pythia_nucleus), not directly comparable to 9-cell means

## 2. Three-Tier Structure (§5 narrative)

### Tier 1: No ordinal signal (perturbation + membership inference)

**DetectGPT** (Mitchell et al. 2023): 9/9 cells, mean 28.8% (chance=25%). Perturbation discrepancy scores measure local token-level sensitivity to paraphrasing — this probes generation artifacts at the token level, not distributional properties across depths. No calibration method (equal-width, CORAL, threshold optimization) exceeds 41.4% on any cell.

**Min-K% Prob** (Shi et al. 2024): 9/9 cells, mean 33.2%. Membership inference scores estimate whether text was in a model's training data — this is orthogonal to how many recursive generation cycles the text has undergone. Slightly above chance due to statistical correlation between depth and token surprisal distributions, but not practically useful.

**Conclusion**: Perturbation sensitivity and training-set membership are token-level properties that do not encode ordinal depth information.

### Tier 2: Partial ordinal signal via implicit distributional encoding (cross-perplexity)

**Binoculars** (Hans et al. 2024): 9/9 cells, three calibration levels:
- Threshold (single score): 69.8% — Binoculars' cross-perplexity ratio implicitly encodes mean-level perplexity distributional displacement. A single threshold already cuts partial ordinal structure because mean perplexity shifts monotonically (though not uniformly) across depths.
- RF_single (1 feature): 63.7% — paradoxically worse than threshold, because RF on a single feature adds variance without information gain.
- RF_multi (11 features): 78.1% — extracting distributional statistics from per-token cross-ppl scores (mean, std, quantiles, etc.) recovers shape-level information. The +8.3pp gain (69.8% → 78.1%) quantifies the marginal contribution of distributional shape beyond mean-level displacement.

**Cross-model robustness**: Binoculars uses pythia-series observer/performer pair, yet gpt2xl cells show the strongest ordinal signal. The cross-ppl depth encoding transfers across model families without retraining — the distributional displacement pattern is model-general.

### Tier 3: Full ordinal signal via purpose-built distributional features

**Our 19-feature RF**: 78.4% (9-cell mean). Captures both mean-level displacement (shared with Binoculars, 6 overlapping features) and shape-level statistics (p90_ppl, var_surprisal, kurtosis, skewness — the dominant depth markers per Depth Degradation Atlas).

**Core signal sharing**: 6/11 Binoculars features ↔ 6/19 our features (mean, median, std, p10, p90, IQR of perplexity distribution). Both capture the same mean-level displacement signal.

**Why the gap is only 0.3pp**: The 6 overlapping features carry most of the depth signal. Our additional shape features (var_surprisal, kurtosis) provide marginal gains; Binoculars' cross-model transfer features provide comparable complementary signal. Neither method's unique features are individually strong enough to create a large accuracy gap.

## 3. Discussion Paragraph: Signal Convergence (§6)

> **Convergence of independent depth signals.** A striking finding emerges from our baseline comparison: Binoculars (Hans et al., 2024), designed for binary AI text detection, achieves 78.1% four-class ordinal depth accuracy when calibrated with a multi-feature Random Forest — within 0.3 percentage points of our purpose-built 19-feature pipeline (78.4%). Feature overlap analysis reveals that 6 of 11 Binoculars-derived features directly correspond to 6 of our 19 features, both capturing mean-level perplexity distributional displacement.
>
> The level-vs-shape decomposition is quantitatively informative. Binoculars' single cross-perplexity score, which implicitly encodes mean-level distributional shift, already achieves 69.8% with simple threshold calibration. Adding distributional shape features via multi-feature RF yields +8.3pp (78.1%), quantifying the marginal contribution of shape-level information. Our features additionally capture shape-level statistics — p90\_ppl, var\_surprisal, kurtosis — which the Depth Degradation Atlas identifies as the dominant depth markers across all 9 settings. That two independent methods — distributional shape statistics and cross-model perplexity agreement — converge on near-identical accuracy strengthens the claim that ordinal depth is a genuine distributional property of recursively generated text. Notably, although Binoculars employs a pythia-series observer/performer pair, the strongest ordinal signal appears in GPT-2 XL cells, demonstrating that the cross-perplexity depth encoding transfers across model families.
>
> By contrast, perturbation-based detection (DetectGPT, 28.8%) and membership inference (Min-K\% Prob, 33.2%) achieve near-chance accuracy. These methods probe local token-level properties — perturbation sensitivity and training-set membership — that do not encode ordinal depth information. The depth signal resides in distributional shape, not in token-level anomalies.

## 5. Updated Narrative Summary

**Old**: "Binary detection methods fail at ordinal depth — the signal requires purpose-built distributional features."

**New**: "Ordinal depth signal is encoded in perplexity distribution shape. Three paradigms tested: perturbation-based (DetectGPT ~29%) and membership-inference (Min-K% 33%) miss it entirely; cross-perplexity (Binoculars) partially captures it via implicit mean-level encoding (threshold 69.8%), with shape-level features adding +8.3pp (RF_multi 78.1%). Our 19-feature pipeline shares a core signal with Binoculars (6/11↔6/19 feature overlap) and adds shape-level statistics (p90_ppl, var_surprisal) for 78.4%. The convergence validates depth as a genuine distributional property."
