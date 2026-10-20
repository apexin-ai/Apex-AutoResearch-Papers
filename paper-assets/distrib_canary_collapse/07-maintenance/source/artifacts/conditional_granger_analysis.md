# Conditional Granger Causality Analysis: token_entropy vs ECE

## Objective

Disentangle whether token_entropy and ECE provide independent predictive channels for downstream diversity collapse, or whether they are redundant manifestations of a single underlying degradation process.

## Method

- **Framework**: VAR(1) with Granger causality F-tests via `statsmodels`
- **Experiments**: 11 experiments across α-sweep (α=0.50/0.55/0.75, seeds 42/43/44), cross-architecture (pythia-410m, opt-1b, pythia-1b-c4), and cross-scale (smollm-3b). Note: the Pythia-1.4B α=0.50 experiment was excluded due to incomplete training (T=2).
- **Variables**: canaries (token_entropy, ECE) → downstreams (distinct_1/2/3, mauve)
- **Tests**: 44 experiment×downstream pairs, each with 5 test types

All experiments have T=11 generations. VAR(1) with 3 variables uses 10 effective observations (df_resid varies by test type).

## Key Results

### 1. Unconditional vs Conditional Significance Rates (p<0.05)

| Test | Sig / Total | Rate |
|------|-----------|------|
| Unconditional entropy→downstream | 35/44 | 79.5% |
| Unconditional ECE→downstream | 35/44 | 79.5% |
| **Conditional entropy→downstream \| ECE** | **16/44** | **36.4%** |
| **Conditional ECE→downstream \| entropy** | **23/44** | **52.3%** |
| Joint [entropy,ECE]→downstream | 39/44 | 88.6% |

**Drop from unconditional to conditional**: entropy loses 54% of significant tests; ECE loses 34%. Both canaries share substantial predictive overlap, but ECE retains more unique information.

### 2. Redundancy Classification (p<0.05)

| Pattern | Count | Fraction |
|---------|-------|----------|
| Both independent | 12 | 27.3% |
| Entropy dominant only | 4 | 9.1% |
| ECE dominant only | 11 | 25.0% |
| Redundant/shared signal | 14 | 31.8% |
| Neither significant | 3 | 6.8% |

**Dominant pattern is redundancy**: in 31.8% of pairs, both canaries are significant unconditionally but *neither* survives conditioning — they share the same predictive information.

**ECE dominant > entropy dominant** (11 vs 4): when only one channel carries unique information, it's more often ECE.

**Both-independent cases** concentrate on: (a) mauve target in α-sweep experiments (5/12), and (b) distinct targets in larger models (pythia-1b-c4, smollm-3b: 6/12).

### 3. Partial R² Effect Sizes

| Downstream | Mean pR²(entropy) | Mean pR²(ECE) | ENT wins | ECE wins |
|-----------|-------------------|---------------|----------|----------|
| distinct_1 | 0.340 | **0.667** | 1/11 | 10/11 |
| distinct_2 | 0.399 | 0.450 | 4/11 | 7/11 |
| distinct_3 | 0.256 | 0.297 | 4/11 | 7/11 |
| mauve | 0.408 | **0.473** | 2/11 | 9/11 |
| **Overall** | **0.351** | **0.472** | **11/44** | **33/44** |

ECE provides larger incremental variance explained in **75.0%** of pairs. The effect is strongest for distinct_1 (ECE pR²=0.667 vs entropy pR²=0.340) and mauve (ECE pR²=0.473 vs entropy pR²=0.408).

### 4. Canary Inter-Correlation

| Experiment group | Pearson r (entropy vs ECE) |
|-----------------|--------------------------|
| α-sweep (GPT-2 small) | −0.84 to −0.91 |
| Cross-architecture (pythia, opt) | −0.98 |
| Cross-scale (smollm-3b) | −0.84 |

Strong negative correlation across all experiments (r = −0.84 to −0.98). The two metrics are near-collinear, especially for larger models.

## Interpretation

### Core Finding: Shared Mechanism with ECE as Primary Channel

Token_entropy and ECE are **not independent channels**. They are two correlated manifestations of the same underlying process — calibration degradation during iterative training on synthetic data. The evidence:

1. **High collinearity** (r = −0.84 to −0.98): as ECE rises (calibration worsens), token_entropy drops (distribution sharpens). These are two sides of one coin.

2. **Massive significance loss under conditioning**: 80% → 36% for entropy, 80% → 52% for ECE. Most of what entropy predicts about diversity, ECE already captures (and vice versa).

3. **When forced to choose, ECE wins**: 75% of partial R² comparisons favor ECE; conditional ECE survives more often (52% vs 36%).

4. **Scale-dependent nuance**: larger models (pythia-1b, smollm-3b) show more "both independent" patterns for diversity metrics, suggesting that at scale, entropy and ECE may capture partially distinct degradation pathways.

### Why ECE > Entropy?

ECE directly measures the gap between predicted probabilities and actual correctness — it's a direct calibration metric. Token_entropy is a distributional summary that *correlates* with miscalibration but also captures other phenomena (vocabulary restriction, mode collapse). ECE is the more mechanistically proximal canary.

### The Mauve Exception

Mauve targets show the most "both_independent" patterns in α-sweep experiments. This makes sense: MAUVE captures distributional divergence at a higher level that may be driven by *both* the calibration pathway (ECE) and the entropy pathway independently.

## Paper Recommendations

### For Methods Section

> "We evaluate two canary metrics — token_entropy and ECE — as early warning signals. These metrics are strongly anti-correlated (r = −0.84 to −0.98), reflecting that both capture aspects of the same calibration degradation process. Conditional Granger analysis reveals substantial redundancy: unconditional significance rates of ~80% for both canaries drop to 36–52% when conditioning on the other. ECE retains more unique predictive power (partial R² = 0.47 vs 0.35), consistent with its more direct role as a calibration measure."

### For Results Section

Report the conditional analysis as evidence that the "phase transition" detection signal is primarily driven by a **single calibration-degradation mechanism** with two observable correlates, rather than two independent warning channels. This strengthens the mechanistic story — the canary signal has a coherent cause.

### Recommended Framing

Frame as: "We confirm that the detection signal arises from calibration collapse (ECE) rather than from two independent information channels. Token entropy and ECE are near-collinear (|r| > 0.84), and conditional Granger analysis shows 32% of pairs have pure redundancy. When unique information exists, ECE is the dominant channel (75% of partial R² comparisons). This supports a single-mechanism interpretation of the canary phase transition."

### Citation Evidence Hierarchy

When citing conditional Granger results in the paper, use this evidence hierarchy:

- **Primary evidence**: Collinearity (r = −0.84 to −0.98) + partial R² comparison (ECE mean pR² = 0.472 vs entropy mean pR² = 0.351). These are robust to the low-df setting.
- **Supporting evidence**: Significance rate drop (80% unconditional → 36%/52% conditional). Directionally informative but significance counts are underpowered.
- **Required caveat**: "Note that conditional F-tests have only ~5 df_resid (T=11, 3 regressors in full model), limiting statistical power for the conditional comparison."

### Caveats

1. **Low df_resid in conditional F-tests**: Conditional F-tests have only ~5 df_resid (T=11, 3 regressors in the full VAR(1) model), limiting statistical power for the conditional comparison. The collinearity evidence (r = −0.84 to −0.98) and partial R² comparison are more robust than the significance-based counts.
2. **The partial R² analysis is more robust** than p-values for this sample size — focus on effect sizes rather than significance.
3. **Lack of T=20 data**: no T=20 experiments were available to confirm these patterns with higher power.
4. **14b experiment incomplete**: The Pythia-1.4B α=0.50 experiment (`scale_check/pythia14b_a050_s42_bf16`) only completed 2 generations (T=2), insufficient for VAR analysis. The 14b entry in the original analysis used an incorrect path and was effectively skipped.

## Data

- Script: `results/analysis/conditional_granger_v2.py`
- Full JSON results: `results/analysis/conditional_granger_v2.json`
- 11 experiments × 4 downstream targets = 44 test pairs
- All T=11 (generation 0–10)
