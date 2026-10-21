# Metrics Summary

Generated from registry.yaml on 2026-05-16

## Baselines

| exp_id | eval_ppl_holdout | eval_loss_holdout | train_loss | conclusion | hypothesis |
|--------|-----------------|-------------------|------------|------------|------------|
| baseline_qwen3_0.6b | 22.9700 | 3.1340 |  | success | Raw Qwen3-0.6B pretrained checkpoint baseline PPL (no continued pretraining). Reference point for quantifying absolut... |

## Uniform Weighting

| exp_id | eval_ppl_holdout | eval_loss_holdout | train_loss | conclusion | hypothesis |
|--------|-----------------|-------------------|------------|------------|------------|
| uniform_seed123 | 17.6861 | 2.8728 | 7.3121 | success | Uniform weighting baseline (no provenance information) for comparison with grid-b and adaptive methods |
| uniform_seed42 | 17.6939 | 2.8732 | 7.3104 | success | Uniform weighting baseline (no provenance information) for comparison with grid-b and adaptive methods |
| uniform_seed456 | 17.7015 | 2.8737 | 7.2895 | success | Uniform weighting baseline (no provenance information) for comparison with grid-b and adaptive methods |

## Adaptive Weighting

| exp_id | eval_ppl_holdout | eval_loss_holdout | train_loss | conclusion | hypothesis |
|--------|-----------------|-------------------|------------|------------|------------|
| adaptive_seed123 | 17.6308 | 2.8696 | 9.2665 | success | Adaptive b* (from α_eff theory) matches or exceeds grid-searched best-b without grid search, seed=123 |
| adaptive_seed456 | 17.6419 | 2.8703 | 9.2354 | success | Adaptive b* (from α_eff theory) matches or exceeds grid-searched best-b without grid search, seed=456 |
| adaptive_fix_seed123 | 17.6432 | 2.8704 |  | success | D012 n_min fix (3→2, batch_size//2): adaptive b* with corrected ESS constraint maintains or improves seed123 performa... |
| adaptive_seed42 | 17.6440 | 2.8704 | 9.2665 | success | Adaptive b* (from α_eff theory) matches or exceeds grid-searched best-b without grid search, seed=42 |
| adaptive_fix_seed42 | 17.6527 | 2.8709 | 7.5167 | success | D012 n_min fix (3→2, batch_size//2): adaptive b* with corrected ESS constraint achieves meaningful improvement over u... |
| adaptive_fix_seed456 | 17.6566 | 2.8711 | 8.3124 | success | D012 n_min fix (3→2, batch_size//2): adaptive b* with corrected ESS constraint maintains or improves seed456 performa... |

## Grid Search (beta)

| exp_id | eval_ppl_holdout | eval_loss_holdout | train_loss | conclusion | hypothesis |
|--------|-----------------|-------------------|------------|------------|------------|
| grid_b0_5_seed123 | 17.6380 | 2.8700 | 9.6010 | success |  |
| grid_b0_5_seed456 | 17.6500 | 2.8705 | 9.5622 | success | Grid-b weighting with b=0.5, seed=456, for multi-seed validation of best-b baseline |
| grid_b1_0_seed123 | 17.6740 | 2.8721 | 10.2180 | success |  |
| grid_b1_0_seed456 | 17.6800 | 2.8734 | 10.1780 | success | Grid-b weighting with b=1.0, seed=456, for multi-seed validation of best-b baseline |
| grid_b1_5_seed123 | 17.7010 | 2.8736 | 10.4776 | success |  |
| grid_b1_5_seed456 | 17.7100 | 2.8750 | 10.4350 | success | Grid-b weighting with b=1.5, seed=456, for multi-seed validation of best-b baseline |
| grid_b2_0_seed123 | 17.7250 | 2.8750 | 10.6100 | success |  |
| grid_b3_0_seed123 | 17.7600 | 2.8770 | 10.7422 | success |  |
| grid_b5_0_seed123 | 17.8039 | 2.8794 | 10.8468 | success |  |
| grid_b3_0_seed456 | 17.9210 | 2.8860 | 5.4350 | success | Grid-b weighting with b=3.0, seed=456, for multi-seed validation of best-b baseline |
| grid_b2_0_seed456 | 17.9890 | 2.8898 | 10.6250 | success | Grid-b weighting with b=2.0, seed=456, for multi-seed validation of best-b baseline |
| grid_b5_0_seed456 | 17.9930 | 2.8900 | 5.4880 | success | Grid-b weighting with b=5.0, seed=456, for multi-seed validation of best-b baseline |
| grid_b_seed42_batch |  |  |  | success | Grid-b weighting with 6 b values (0.5, 1.0, 1.5, 2.0, 3.0, 5.0) for seed=42, establishes best-b baseline for comparis... |

## Tau Sweep

| exp_id | eval_ppl_holdout | eval_loss_holdout | train_loss | conclusion | hypothesis |
|--------|-----------------|-------------------|------------|------------|------------|
| tau_07_seed42 | 17.6793 | 2.8724 | 9.6707 | success | τ sensitivity sweep: τ=0.7 (slightly below baseline), testing if moderate τ reduction improves or degrades PPL. Basel... |
| tau_06_seed42 | 17.6805 | 2.8725 | 9.2750 | success | τ sensitivity sweep: τ=0.6 (lower α_eff threshold) may allow more aggressive downweighting, testing if PPL improves o... |
| tau_05_seed42 | 17.6880 | 2.8729 | 8.8490 | success | τ sensitivity sweep: τ=0.5 (most permissive α_eff threshold), testing lower bound of useful τ range. Baseline τ=0.8 P... |

## Contamination

| exp_id | eval_ppl_holdout | eval_loss_holdout | train_loss | conclusion | hypothesis |
|--------|-----------------|-------------------|------------|------------|------------|
| contamination_60_grid_b0_5_seed42 | 17.7040 | 2.8738 |  | success | ρ=0.6 grid-best (b=0.5) baseline: fixed b=0.5 on 60% contamination. Tests if grid-optimal b from ρ=0.4 transfers to h... |
| contamination_60_seed42_r2 | 17.7400 | 2.8759 | 9.6349 | success | Retry of contamination_60_seed42 (failed due to GPU conflict on cuda:2). ρ=0.6 adaptive weighting (τ=0.8, n_min=2) on... |
| contamination_60_uniform_seed42 | 17.7660 | 2.8773 | 7.6490 | success | ρ=0.6 uniform baseline: no reweighting on 60% contamination data. Establishes baseline PPL degradation at higher cont... |
| contamination_60_ess_only_seed42 | 17.7700 | 2.8775 | 9.8420 | success | ESS-only (max-intervention) on ρ=0.6 data: b* = max{b : ESS(b) ≥ n_min}. Tests if dual-constraint advantage over ESS-... |

## N_min Ablation

| exp_id | eval_ppl_holdout | eval_loss_holdout | train_loss | conclusion | hypothesis |
|--------|-----------------|-------------------|------------|------------|------------|
| nmin4_seed42 | 17.6947 | 2.8733 | 7.9890 | success | n_min=4 (=batch_size) ablation: forces b*=0 always since ESS constraint cannot be satisfied with any b>0 when n_min=b... |
| nmin1_seed42 | 17.7890 | 2.8786 |  | success | n_min=1 sensitivity: minimal ESS constraint allows more aggressive downweighting, testing if adaptive method degrades... |

## Other

| exp_id | eval_ppl_holdout | eval_loss_holdout | train_loss | conclusion | hypothesis |
|--------|-----------------|-------------------|------------|------------|------------|
| golden_ratio_seed42 | 17.6540 | 2.8710 | 2.1145 | success | Golden Ratio oracle baseline: w=1/φ≈0.618 for synthetic (q>0.5), w=1.0 for real — requires known proportion, serves a... |
| ess_only_seed456 | 17.7190 | 2.8746 | 10.1740 | success | ESS-only (max-intervention) seed456: b* = max{b : ESS(b) ≥ n_min} — proves dual-constraint adaptive (min-intervention... |
| ess_only_seed123 | 17.7200 | 2.8746 | 10.2159 | success |  |
| ess_only_seed42 | 17.7300 | 2.8750 |  | success | ESS-only adaptive baseline (max-intervention): b* = max{b : ESS(b) ≥ n_min} — proves min-intervention (adaptive) supe... |
| p0_contamination_60_datagen |  |  |  | success |  |
| detector_tfidf_lr |  |  |  | success | TF-IDF + LogisticRegression detector provides spread q-scores (AUC~0.94, not binarized) for provenance weighting, rep... |
| datagen_synthetic_4gpu |  |  |  | success |  |

