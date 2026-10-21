# Analysis: alpha_sweep_a010_s42_v2

## 1. Training Completion

- **Status**: Completed successfully (EXIT_CODE=0)
- **Generations**: 11 (gen_0 through gen_10), all present
- **Config**: Pythia-410M, WikiText-103, seed=42, synthetic_ratio=0.10, 10 generations x 5000 steps
- **Runtime**: ~4.5h (22:56 to 03:32 UTC, May 18-19 2026)
- **Errors**: None (padding_side warnings are benign and consistent across all runs)
- **Checkpoint**: `results/alpha_sweep/a010_s42/gen_10/checkpoint/` (model.safetensors present)

## 2. Per-Generation Metrics

| Gen | token_entropy | distinct_1 | distinct_2 | distinct_3 | perplexity | ece    | effective_rank | mauve  |
|-----|--------------|------------|------------|------------|------------|--------|----------------|--------|
| 0   | 3.2342       | 0.0982     | 0.5178     | 0.8127     | 26.949     | 0.0108 | 46.613         | 0.0341 |
| 1   | 2.9933       | 0.0975     | 0.5141     | 0.8104     | 19.168     | 0.0090 | 48.819         | 0.0323 |
| 2   | 3.0112       | 0.0814     | 0.4353     | 0.7262     | 19.821     | 0.0114 | 49.336         | 0.0316 |
| 3   | 3.0242       | 0.0737     | 0.3748     | 0.6244     | 20.355     | 0.0118 | 48.697         | 0.0302 |
| 4   | 3.0412       | 0.0676     | 0.3237     | 0.5331     | 20.644     | 0.0126 | 48.747         | 0.0262 |
| 5   | 3.0464       | 0.0641     | 0.2818     | 0.4508     | 20.955     | 0.0143 | 48.186         | 0.0217 |
| 6   | 3.0402       | 0.0620     | 0.2637     | 0.4168     | 20.632     | 0.0131 | 46.179         | 0.0205 |
| 7   | 3.0605       | 0.0608     | 0.2471     | 0.3808     | 20.849     | 0.0154 | 45.957         | 0.0178 |
| 8   | 3.0500       | 0.0599     | 0.2355     | 0.3561     | 21.221     | 0.0160 | 45.847         | 0.0175 |
| 9   | 3.0538       | 0.0592     | 0.2290     | 0.3431     | 21.168     | 0.0168 | 46.091         | 0.0158 |
| 10  | 3.0641       | 0.0593     | 0.2256     | 0.3342     | 21.291     | 0.0170 | 45.175         | 0.0155 |

### Trajectory Notes

- **token_entropy**: Sharp drop gen0->gen1 (3.234->2.993), then gradual recovery to ~3.06 by gen10. Net change: -5.3%.
- **distinct_1**: Monotonic decline, steepest gen1->gen4, plateaus gen7+. Net change: -39.7%.
- **distinct_2/3**: Steep monotonic decline throughout. Net: -56.4% / -58.9%.
- **perplexity**: Sharp drop gen0->gen1, stable ~20-21 thereafter. Net: -21.0%.
- **ece**: Gradual increase (worsening calibration). Net: +57.2%.
- **effective_rank**: Slight decline (-3.1%), no dramatic collapse.

## 3. Comparison with Baselines

| Metric              | α=0.00 s42 | α=0.10 s42 | α=0.25 s43 | α=0.25 s44 | α=0.50 s42 | α=0.75 s42 |
|---------------------|-----------|-----------|-----------|-----------|-----------|-----------|
| gen10 token_entropy | 3.0693    | 3.0641    | 3.0723    | 3.0721    | 2.632     | 2.337     |
| Δ entropy (%)       | -5.1%     | -5.3%     | -5.0%     | -5.0%     | -18.6%    | -27.8%    |
| gen10 distinct_1    | 0.0847    | 0.0593    | 0.0585    | 0.0588    | -         | -         |
| Δ distinct_1 (%)    | -13.8%    | **-39.7%** | -40.5%    | -40.0%    | -         | -         |
| gen10 distinct_2    | 0.4672    | 0.2256    | 0.2236    | 0.2270    | -         | -         |
| Δ distinct_2 (%)    | -9.8%     | **-56.4%** | -56.4%    | -55.8%    | -         | -         |
| gen10 distinct_3    | 0.7760    | 0.3342    | 0.3330    | 0.3364    | -         | -         |
| Δ distinct_3 (%)    | -4.5%     | **-58.9%** | -58.7%    | -58.2%    | -         | -         |
| gen10 perplexity    | 21.108    | 21.291    | 21.899    | 21.984    | -         | -         |
| gen10 ece           | 0.0164    | 0.0170    | 0.0215    | 0.0180    | -         | -         |
| gen10 eff_rank      | 44.817    | 45.175    | 45.367    | 44.354    | -         | -         |
| PermG sig (diff.)   | 0         | 0         | 0         | -         | boundary  | strong    |

### Key Observations

1. **Token entropy is null-like.** gen10=3.0641 vs null gen10=3.0693, a difference of only 0.005 (0.17%). The entropy canary does not respond to α=0.10 contamination.

2. **Diversity collapse matches α=0.25.** distinct_1 drops 39.7% (vs null's 13.8%), nearly identical to α=0.25's 40.0-40.5%. distinct_2 and distinct_3 show the same pattern. At α=0.10, diversity degradation has already reached the α=0.25 plateau.

3. **Perplexity and calibration are near-null.** Perplexity (21.29 vs 21.11) and ECE (0.017 vs 0.016) show minimal deviation from the null baseline.

4. **Diversity collapse is non-linear in α.** The jump from α=0.00 (-13.8% d1) to α=0.10 (-39.7% d1) is far larger than the jump from α=0.10 to α=0.25 (-40.5% d1). Even 10% contamination saturates the diversity collapse channel.

## 4. Permutation Granger Causality Results

### Differenced (valid for causal inference)

| Pair                              | F        | p      | f2      | sig |
|-----------------------------------|----------|--------|---------|-----|
| token_entropy -> distinct_1       | 135.677  | 0.0590 | 22.613  |     |
| distinct_1 -> token_entropy       | 1.072    | 0.3647 | 0.179   |     |
| token_entropy -> distinct_2       | 85.183   | 0.0606 | 14.197  |     |
| distinct_2 -> token_entropy       | 0.577    | 0.4759 | 0.096   |     |
| token_entropy -> distinct_3       | 10.575   | 0.0716 | 1.763   |     |
| distinct_3 -> token_entropy       | 0.127    | 0.7171 | 0.021   |     |
| token_entropy -> effective_rank   | 1.142    | 0.2206 | 0.190   |     |
| effective_rank -> token_entropy   | 0.617    | 0.4681 | 0.103   |     |
| ece -> distinct_1                 | 4.400    | 0.0752 | 0.733   |     |
| distinct_1 -> ece                 | 0.826    | 0.3723 | 0.138   |     |
| ece -> distinct_2                 | 4.332    | 0.0808 | 0.722   |     |
| distinct_2 -> ece                 | 0.255    | 0.6193 | 0.043   |     |
| ece -> distinct_3                 | 1.814    | 0.2254 | 0.302   |     |
| distinct_3 -> ece                 | 0.009    | 0.9336 | 0.001   |     |
| ece -> effective_rank             | 2.067    | 0.1962 | 0.345   |     |
| effective_rank -> ece             | 0.024    | 0.8786 | 0.004   |     |

**Result: 0/16 pairs significant at p<0.05 (differenced).**

Notable: token_entropy -> distinct_1/2/3 show large F-statistics but p-values are marginal (0.059-0.072). The F-statistics are inflated by the short series (T=11, df_resid=6 after differencing+lag), not by genuine predictive power. This matches the α=0.25 pattern (no PermG signal) and contrasts with α=0.50+ where PermG becomes significant.

### Undifferenced (for reference only, not valid for causal claims due to trending)

Multiple pairs show significance in undifferenced mode, but this is expected for any trending time series and does not indicate causal structure.

## 5. Conclusion

**Verdict: Informative negative (success as a map-gap fill)**

α=0.10 behaves like a null control on the **canary channel** (token_entropy, PermG) but matches α=0.25 on the **diversity collapse channel** (distinct_1/2/3). This reveals a critical dissociation:

- **Diversity collapse saturates early**: even 10% synthetic contamination produces ~40% distinct_1 drop, indistinguishable from 25% contamination.
- **The entropy canary is blind below α=0.25**: the detection threshold lies between α=0.25 (no signal) and α=0.50 (boundary signal). At α=0.10, entropy is within 0.2% of the null baseline.
- **Implication for the paper**: the canary (entropy-based Granger) detects contamination only in regimes where the damage is already severe (α>=0.50). The diversity collapse itself begins much earlier but is not "signaled" by the entropy canary until contamination reaches a critical mass.

## 6. Suggested Metrics Dict (for update_registry)

```json
{
  "gen0_token_entropy": 3.2342,
  "gen10_token_entropy": 3.0641,
  "gen0_perplexity": 26.949,
  "gen10_perplexity": 21.291,
  "gen0_distinct_1": 0.0982,
  "gen10_distinct_1": 0.0593,
  "gen0_distinct_2": 0.5178,
  "gen10_distinct_2": 0.2256,
  "gen0_distinct_3": 0.8127,
  "gen10_distinct_3": 0.3342,
  "gen0_ece": 0.0108,
  "gen10_ece": 0.0170,
  "gen0_effective_rank": 46.613,
  "gen10_effective_rank": 45.175,
  "gen0_mauve": 0.0341,
  "gen10_mauve": 0.0155,
  "delta_token_entropy_pct": -5.3,
  "delta_distinct_1_pct": -39.7,
  "delta_distinct_2_pct": -56.4,
  "delta_distinct_3_pct": -58.9,
  "permg_diff_sig_pairs": 0,
  "permg_diff_total_pairs": 16,
  "conclusion": "informative_negative",
  "checkpoint_path": "results/alpha_sweep/a010_s42/gen_10/checkpoint/"
}
```
