# uniform_1_7b_seed123 Analysis

## Final Metrics
- eval_ppl_holdout: **13.26** (13.2648)
- eval_loss_holdout: **2.5851**
- train_loss_final: 7.557
- total_steps: 6103
- train_runtime: 17610s (4h53m)
- num_eval_tokens: 4,077,068

## 1.7B Scale Comparison (2-seed)

| Method | seed42 | seed123 | Mean±Std |
|--------|--------|---------|----------|
| Adaptive | 13.27 | 13.25 | 13.26±0.01 |
| Uniform | 13.50* | 13.26 | 13.38±0.12 |
| Δ (adaptive − uniform) | −0.23 | −0.01 | −0.12±0.11 |

\* seed42 uniform is Plan B (resumed optimizer), not a clean from-scratch run.

### Loss Comparison

| Method | seed42 | seed123 |
|--------|--------|---------|
| Adaptive | 2.5853 | 2.5843 |
| Uniform | — | 2.5851 |
| Δ loss | — | −0.0008 |

## Conclusion

**Weakly positive, with critical caveats.**

- At seed123 (both from-scratch, fair comparison): adaptive PPL (13.25) < uniform PPL (13.26), Δ = −0.01. Technically adaptive wins, but the margin is negligible.
- At seed42: Δ = −0.23 was large, but the uniform baseline had the Plan B optimizer confound (resumed optimizer state), inflating its PPL.
- The seed123 from-scratch uniform result (13.26) is dramatically lower than the seed42 Plan B uniform (13.50), confirming the optimizer resume issue caused ~0.24 PPL degradation.
- **The adaptive advantage at 1.7B scale is not robust**: the fair seed123 comparison shows near-zero difference (Δ = −0.01).
- Cross-seed mean Δ = −0.12±0.11 is dominated by the confounded seed42 run.

**Implication for paper**: The 1.7B result does not strongly support the hypothesis that adaptive weighting improves over uniform at scale. The paper should either (a) acknowledge this as a scaling limitation, or (b) focus the 1.7B narrative on the confound analysis showing optimizer state sensitivity.

## Checkpoint Path
/root/autodl-tmp/provenance_weight_training/output/models/uniform_1_7b_seed123/final

## Log Path
~/runs/provenance_weight_training/uniform_1_7b_seed123.log

## Eval Results Path
/root/provenance_weight_training/eval_perplexity_results_uniform_1_7b_seed123.json
