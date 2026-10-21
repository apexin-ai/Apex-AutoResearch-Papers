# D220 α_crit Proposition Correction Notes

## Correction 1: SC Δ Definition Error (Reviewer #38)

**Problem**: Δ_SC was defined as `θ2n_select_f1 − greedy_f1` (consensus-based sample selection minus greedy). This measures a *selection method* gain, not the actual self-consistency aggregation gain.

**Fix**: Δ_SC = `mv_f1 − greedy_f1` (entity-level majority voting F1 minus greedy F1). This is the correct metric because the α_crit proposition is about SC aggregation (majority voting), not sample selection.

### Before/After Comparison

| Dataset | Δ_SC (old: θ2n−greedy) | Δ_SC (new: MV−greedy) | Empirical (old) | Empirical (new) |
|---------|-------------------------|------------------------|-----------------|-----------------|
| FewNERD | **+0.89 pp** | **−9.21 pp** | Yes | **No** |
| CoNLL   | **−1.09 pp** | **−1.37 pp** | No | No |
| SciERC  | **+0.76 pp** | **−3.03 pp** | Yes | **No** |

### Unchanged Values

α_crit formula, π_MV, α_obs, α_crit, Gap, Degeneracy — all unchanged. The Detailed Baselines table is also unchanged (MV and greedy values were already correct; only the Δ_SC column in the Main Table was computed from the wrong pair).

## Impact on Paper Conclusions

**Strengthens the narrative.** The old table showed a mixed picture (2/3 confirm bound, 1/3 violates). The corrected table shows **universal failure**: the bound predicts SC should work for all three datasets, but it never does.

This has two implications:

1. **Degeneracy-adjusted bound**: Still correctly explains CoNLL (δ=63% → α_crit_eff=2.184 > 1). But now FewNERD and SciERC also fail despite having low degeneracy (12.3%, 20.3%) — degeneracy alone is insufficient as an explanation.

2. **Structural mismatch**: Entity-level MV is fundamentally different from classification-level SC. When span boundaries differ across samples, MV introduces aggregation errors absent from any individual sample. This is a novel mechanism not present in standard SC literature (where MV over complete outputs preserves internal consistency).

3. **Sample-level selection can still work**: LP selection achieves +1.36 pp on FewNERD (p<0.05) despite MV failing at −9.21 pp. Selection preserves span consistency within each sample while still exploiting confidence signal variation across samples. This contrast between aggregation failure and selection success is a key diagnostic finding.

## No Changes Needed for Other Propositions

The α_crit formula `α_crit = π_MV / (2 − π_MV)` and the degeneracy-adjusted variant `α_crit_eff = α_crit / (1 − δ)` are mathematically correct. The error was purely in the empirical validation metric (using θ2n instead of MV).
