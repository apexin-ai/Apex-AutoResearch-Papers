# Adaptive Temperature Protocol — Evaluation Report

## Hypothesis
High-degeneracy datasets benefit from T=1.2: lower degeneracy enables better LP (log-probability) selection, yielding higher F1 than greedy decoding at T=1.0.

## Protocol
1. Compute T=1.0 degeneracy rate (all N=8 samples produce identical entity sets after gold-empty filtering)
2. If degeneracy > 30% → switch to T=1.2; otherwise keep T=1.0
3. Compare: LP selection F1 at adaptive T vs. greedy F1 at T=1.0
4. Span-based (start, end, type) F1, gold_filter=True, Bootstrap 10K resamples for 95% CI

## Summary Table

| Dataset   | Degen@T1.0 | Switch? | Greedy F1 | LP@AdaptT | Delta (pp) | 95% CI            |
|-----------|------------|---------|-----------|-----------|------------|-------------------|
| SciERC    | 11.7%      | no      | 0.6442    | 0.6468    | +0.26      | [-1.13, +1.65] NS |
| CoNLL2003 | 60.6%      | YES     | 0.9077    | 0.8976    | **-1.01**  | [-1.49, -0.55] ** |
| FewNERD   | 9.4%       | no      | 0.7480    | 0.7624    | **+1.44**  | [+1.26, +1.61] ** |

## Key Findings

### 1. Hypothesis REFUTED for CoNLL (the only switching dataset)
- CoNLL degeneracy: 60.6% → 49.6% at T=1.2 (11 pp reduction)
- Despite degeneracy reduction, LP selection at T=1.2 **underperforms** greedy at T=1.0 by -1.01 pp
- CI entirely negative: [-1.49, -0.55], p=1.0 (LP ≤ Greedy)
- Interpretation: higher temperature diversifies samples but introduces lower-quality outputs; LP cannot reliably identify the best sample

### 2. FewNERD: LP selection works at T=1.0 without switching
- Low degeneracy (9.4%) already provides diverse samples at T=1.0
- LP selection gains +1.44 pp over greedy (CI [+1.26, +1.61], highly significant)
- This is the strongest evidence that LP selection is viable, but the gain comes from natural diversity at standard temperature, not from temperature tuning

### 3. SciERC: neutral
- Low degeneracy (11.7%), no switch
- LP selection +0.26 pp, not significant (CI [-1.13, +1.65])
- Small dataset (529 gold-filtered instances) limits statistical power

## Degeneracy Reduction by T=1.2

| Dataset   | T=1.0 Degen | T=1.2 Degen | Reduction |
|-----------|------------|------------|-----------|
| SciERC    | 11.7%      | 10.4%      | 1.3 pp    |
| CoNLL2003 | 60.6%      | 49.6%      | 11.0 pp   |
| FewNERD   | 9.4%       | pending    | pending   |

## Implications
- The adaptive temperature protocol does NOT improve performance. The only dataset that triggers switching (CoNLL) gets worse.
- LP selection works best on datasets with moderate natural diversity (FewNERD), not on datasets forced into diversity via higher temperature.
- Greedy decoding remains a strong baseline — for high-degeneracy datasets, the problem may be model capacity/calibration rather than sampling temperature.

## Data Sources
- SciERC T=1.0: exp_001_seed42_v2 (N=16, subsampled to 8)
- SciERC T=1.2: exp_026_t12 (N=8)
- CoNLL T=1.0: exp_002_conll_n8_seed123 (N=8)
- CoNLL T=1.2: exp_030_conll_t12 (N=8)
- FewNERD T=1.0: exp_021_fewnerd_n8_seed123 (N=8)
- FewNERD T=1.2: exp_031_fewnerd_t12 (N=8, inference in progress)

## Note
FewNERD T=1.2 inference is still running (~6.6% complete, ~1.5h remaining). Since FewNERD degeneracy is 9.4% < 30% threshold, the adaptive protocol keeps T=1.0 regardless. The T=1.2 data will be useful for ablation comparison but does not affect the adaptive protocol results.

JSON results: output/adaptive_temperature_results.json
