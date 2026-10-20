# E1v2: Signal Routing with Deployment-Available Features

## Key Change
Removed all ground-truth-dependent features (oracle_headroom, base_f1, rho_*).
Replaced with deployment-available features: lp_variance, vc_variance + interactions.

## Features (8 total)
- **Base (5)**: model_size, regime, degeneracy_rate, lp_variance, vc_variance
- **Interactions (3)**: model_size×regime, regime×degeneracy, model_size×degeneracy

## Results

| Model | LOO Acc | 5-fold CV | Router dF1 | Always-LP dF1 | Oracle dF1 |
|-------|---------|-----------|------------|---------------|------------|
| GradientBoosting | 56.2% (9/16) | 55.0% ± 17.9% | +0.36pp | +0.15pp | +0.56pp |
| RandomForest | 68.8% (11/16) | 68.3% ± 21.3% | +0.37pp | +0.15pp | +0.56pp |

## E1 vs E1v2 Comparison

| Metric | E1 (RF, LOO) | E1v2 GB (LOO) | E1v2 RF (LOO) |
|--------|-------------|---------------|---------------|
| Accuracy | 56.2% | 56.2% | 68.8% |
| Router dF1 | +0.39pp | +0.36pp | +0.37pp |
| Features | 12 (incl. oracle) | 8 (deploy-only) | 8 (deploy-only) |

## Top Features (GradientBoosting)
- degeneracy_rate: 0.3211
- model_size×degeneracy: 0.1718
- vc_variance: 0.1357
- model_size: 0.1234
- model_size×regime: 0.0940

## Top Features (RandomForest)
- model_size×degeneracy: 0.2452
- degeneracy_rate: 0.1960
- regime×degeneracy: 0.1415
- vc_variance: 0.0992
- model_size×regime: 0.0868

## Data Notes
- 7/16 configs had raw samples.jsonl available for variance computation
- 9 configs used regime-group mean imputation for lp_variance/vc_variance
- Only FT 8B Qwen3 configs had raw samples; 72B (ZS/FS) and 7B configs were imputed

## Regime Patterns
- **FT** (10 configs): {'consensus_theta2n': 3, 'none': 2, 'lp_selection': 5}
- **ZS** (3 configs): {'consensus_lp_weighted': 1, 'none': 2}
- **FS** (3 configs): {'none': 1, 'lp_selection': 1, 'majority_vote': 1}
