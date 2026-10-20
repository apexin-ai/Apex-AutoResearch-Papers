# Conditional Granger Causality Analysis: token_entropy vs ECE

## Objective

Disentangle whether token_entropy and ECE provide independent predictive channels for downstream diversity collapse, or whether they are redundant manifestations of a single underlying degradation process.

## Method

- **Framework**: VAR(1) with Granger causality F-tests via `statsmodels`
- **Experiments**: 12 experiments across α-sweep (α=0.50/0.55/0.75, seeds 42/43/44), cross-architecture (pythia-410m, opt-1b, pythia-1b-c4), and cross-scale (pythia-1.4b, smollm-3b)
- **Variables**: canaries (token_entropy, ECE) → downstreams (distinct_1/2/3, mauve)
- **Tests**: 48 experiment×downstream pairs, each with 5 test types

All experiments have T=11 generations. VAR(1) with 3 variables uses 10 effective observations (df_resid varies by test type).

## Key Results

### 1. Unconditional vs Conditional Significance Rates (p<0.05)

| Test | Sig / Total | Rate |
|------|-----------|------|
| Unconditional entropy→downstream | 38/48 | 79.2% |
| Unconditional ECE→downstream | 38/48 | 79.2% |
| **Conditional entropy→downstream \| ECE** | **17/48** | **35.4%** |
| **Conditional ECE→downstream \| entropy** | **23/48** | **47.9%** |
| Joint [entropy,ECE]→downstream | 42/48 | 87.5% |

**Drop from unconditional to conditional**: entropy loses 55% of significant tests; ECE loses 39%. Both canaries share substantial predictive overlap, but ECE retains more unique information.

### 2. Redundancy Classification (p<0.05)

| Pattern | Count | Fraction |
|---------|-------|----------|
| Both independent | 12 | 25.0% |
| Entropy dominant only | 5 | 10.4% |
| ECE dominant only | 11 | 22.9% |
| Redundant/shared signal | 16 | 33.3% |
| Neither significant | 4 | 8.3% |

**Dominant pattern is redundancy**: in 33.3% of pairs, both canaries are significant unconditionally but *neither* survives conditioning — they share the same predictive information.

**ECE dominant > entropy dominant** (11 vs 5): when only one channel carries unique information, it's more often ECE.

**Both-independent cases** concentrate on: (a) mauve target in α-sweep experiments (5/12), and (b) distinct targets in larger models (pythia-1b-c4, smollm-3b: 6/12).

### 3. Partial R² Effect Sizes

| Downstream | Mean pR²(entropy) | Mean pR²(ECE) | ENT wins | ECE wins |
|-----------|-------------------|---------------|----------|----------|
| distinct_1 | 0.330 | **0.646** | 1/12 | 11/12 |
| distinct_2 | 0.405 | 0.413 | 5/12 | 7/12 |
| distinct_3 | 0.252 | 0.273 | 5/12 | 7/12 |
| mauve | 0.395 | **0.462** | 2/12 | 10/12 |
| **Overall** | **0.346** | **0.448** | **13/48** | **35/48** |

ECE provides larger incremental variance explained in **72.9%** of pairs. The effect is strongest for distinct_1 (ECE pR²=0.646 vs entropy pR²=0.330) and mauve (ECE pR²=0.462 vs entropy pR²=0.395).

### 4. Canary Inter-Correlation

| Experiment group | Pearson r (entropy vs ECE) |
|-----------------|--------------------------|
| α-sweep (GPT-2 small) | −0.84 to −0.91 |
| Cross-architecture (pythia, opt) | −0.98 |
| Cross-scale (1.4b, 3b) | −0.84 to −0.90 |

Strong negative correlation across all experiments (r = −0.84 to −0.98). The two metrics are near-collinear, especially for larger models.

## Interpretation

### Core Finding: Shared Mechanism with ECE as Primary Channel

Token_entropy and ECE are **not independent channels**. They are two correlated manifestations of the same underlying process — calibration degradation during iterative training on synthetic data. The evidence:

1. **High collinearity** (r = −0.84 to −0.98): as ECE rises (calibration worsens), token_entropy drops (distribution sharpens). These are two sides of one coin.

2. **Massive significance loss under conditioning**: 79% → 35% for entropy, 79% → 48% for ECE. Most of what entropy predicts about diversity, ECE already captures (and vice versa).

3. **When forced to choose, ECE wins**: 73% of partial R² comparisons favor ECE; conditional ECE survives more often (48% vs 35%).

4. **Scale-dependent nuance**: larger models (pythia-1b, smollm-3b) show more "both independent" patterns for diversity metrics, suggesting that at scale, entropy and ECE may capture partially distinct degradation pathways.

### Why ECE > Entropy?

ECE directly measures the gap between predicted probabilities and actual correctness — it's a direct calibration metric. Token_entropy is a distributional summary that *correlates* with miscalibration but also captures other phenomena (vocabulary restriction, mode collapse). ECE is the more mechanistically proximal canary.

### The Mauve Exception

Mauve targets show the most "both_independent" patterns (5/12 in α-sweep). This makes sense: MAUVE captures distributional divergence at a higher level that may be driven by *both* the calibration pathway (ECE) and the entropy pathway independently.

## Paper Recommendations

### For Methods Section

> "We evaluate two canary metrics — token_entropy and ECE — as early warning signals. These metrics are strongly anti-correlated (r = −0.84 to −0.98), reflecting that both capture aspects of the same calibration degradation process. Conditional Granger analysis reveals substantial redundancy: unconditional significance rates of ~79% for both canaries drop to 35–48% when conditioning on the other. ECE retains more unique predictive power (partial R² = 0.45 vs 0.35), consistent with its more direct role as a calibration measure."

### For Results Section

Report the conditional analysis as evidence that the "phase transition" detection signal is primarily driven by a **single calibration-degradation mechanism** with two observable correlates, rather than two independent warning channels. This strengthens the mechanistic story — the canary signal has a coherent cause.

### Recommended Framing

Frame as: "We confirm that the detection signal arises from calibration collapse (ECE) rather than from two independent information channels. Token entropy and ECE are near-collinear (|r| > 0.84), and conditional Granger analysis shows 33% of pairs have pure redundancy. When unique information exists, ECE is the dominant channel (73% of partial R² comparisons). This supports a single-mechanism interpretation of the canary phase transition."

### Caveats

1. **T=11 is short**: VAR(1) with 3 variables leaves only ~4 residual df for the conditional F-test. Effect sizes are large (pR² > 0.3) which helps, but exact p-values should be interpreted cautiously.
2. **The partial R² analysis is more robust** than p-values for this sample size — focus on effect sizes rather than significance.
3. **Lack of T=20 data**: no T=20 experiments were available to confirm these patterns with higher power.

## Data

- Script: `results/analysis/conditional_granger_v2.py`
- Full JSON results: `results/analysis/conditional_granger_v2.json`
- 12 experiments × 4 downstream targets = 48 test pairs
- All T=11 (generation 0–10)
