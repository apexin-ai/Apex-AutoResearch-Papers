# D220 α_crit Proposition Correction Notes

## Correction History

### v1 → v2: SC Δ Definition Error (Reviewer #38)

**Problem**: Δ_SC was defined as `θ2n_select_f1 − greedy_f1` (consensus-based sample selection minus greedy). This measures a *selection method* gain, not SC aggregation gain.

**Fix**: Δ_SC = `mv_f1 − greedy_f1` (entity-level majority voting F1 minus greedy F1).

| Dataset | Δ_SC v1 (θ2n−greedy) | Δ_SC v2 (MV−greedy, macro) | Empirical v1 | Empirical v2 |
|---------|----------------------|---------------------------|--------------|--------------|
| FewNERD | +0.89 pp | −9.21 pp | Yes | No |
| CoNLL   | −1.09 pp | −1.37 pp | No | No |
| SciERC  | +0.76 pp | −3.03 pp | Yes | No |

v2 conclusion: "SC universally fails" (3/3 negative Δ).

### v2 → v3: macro_f1 → micro_f1 (Reviewer #47)

**Problem**: v2 used macro-F1 data from MF4 pipeline (which had a greedy_macro_f1 bug). Macro-F1 averages per-instance F1, dramatically over-weighting instances with few entities where MV produces empty outputs → inflated negative Δ.

**Fix**: Recomputed all metrics using MF4v2 pipeline data with micro-F1 (aggregate TP/FP/FN then compute F1).

| Dataset | Δ_SC v2 (macro) | Δ_SC v3 (micro) | Direction Change |
|---------|-----------------|-----------------|------------------|
| FewNERD | −9.21 pp | −0.83±0.38 pp | Same sign, 11× smaller |
| CoNLL   | −1.37 pp | +0.16±0.17 pp | **Sign flip** (neg → pos) |
| SciERC  | −3.03 pp | +0.15±0.18 pp | **Sign flip** (neg → pos) |

v3 conclusion: MV ≈ greedy (|Δ| < 1pp). SC is not "universally failing" — it's approximately neutral. The real limitation is that MV captures negligible fraction of oracle headroom (4–11pp), not that it catastrophically degrades.

## Impact on Paper Narrative

| Claim | v2 (macro, wrong) | v3 (micro, correct) |
|-------|-------------------|---------------------|
| SC aggregation effect | "universally fails" | "approximately neutral" |
| MV vs greedy | −1.4 to −9.2pp | ±0.8pp |
| α_crit bound validity | "predicts success, observes failure" | "consistent — marginal signals, marginal gains" |
| Core insight | SC destroys quality | SC neither helps nor hurts; bottleneck is alignment, not aggregation |

The corrected narrative is actually **stronger** for the paper's main claim: "correlation ≠ selection." Under micro-F1, MV is at parity with greedy despite moderate agreement correlations (ρ=0.31–0.46), which means the signals *detect* quality variation but cannot *translate* it into improvement via aggregation. This is a more nuanced and defensible claim than "SC universally fails."
