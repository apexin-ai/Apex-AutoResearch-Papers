# Training Loss vs Closed-Loop SR Analysis

## Data Source

- **Training loss**: Extracted from project decision logs (`decisions.yaml`), progress reports, and running status snapshots. Original training stdout was not saved to file (printed to tmux, lost after session). Checkpoint files (`crm_best.pt`) contain only `state_dict` without metrics history.
- **Key sources**: `decisions.yaml` (best_epoch, val_loss), `report_running_status.md` (mid-training snapshots with train_loss), `results_tables.md` (closed-loop SR)
- **Training config**: 50 epochs, batch_size=32, lr=1e-3 (cosine decay), val_split=0.1, aug_ratio=0.5, 26,737 samples (spatial 12,167 + object 14,570)
- **Checkpoint location**: `/root/autodl-tmp/checkpoints/crm_v3_norm/{perdof,obs_only,scalar_unc}/crm_best.pt` on bjb1-18228
- **Version**: CRM v3-norm (with input normalization via input_mean/input_std, post-D018 fix)

## Results Table

| Variant | Val MSE (best) | Best Epoch | Train MSE (ep24 snapshot) | Object SR seed42 | Object SR (multi-seed mean) | Spatial SR seed42 |
|---------|:-:|:-:|:-:|:-:|:-:|:-:|
| **obs_only** | **0.0165** | 48 | 0.0265 | **19%** | **17.5%** (4 seeds, ε=0.2) | **35%** |
| perdof (full) | 0.0358 | 47 | ~0.054 (est.) | 11% | 10.3% (3 seeds) | 35% |
| scalar (scalar_unc) | 0.0374 | 46 | 0.0592 | 9% | 8.0% (2 seeds) | 32% |

### Baselines (no CRM correction)

| Baseline | Object SR seed42 | Object SR (multi-seed) | Spatial SR seed42 |
|----------|:-:|:-:|:-:|
| argmin (K=10 selection) | 12% | 14.0% (3 seeds) | 34% |
| VLA-mean (K=10 average) | 12% | 12.3% (3 seeds) | 32% |
| VLA-only (K=1, no ensemble) | 12% | 10.8% (4 seeds) | 30% |

### Notes on Train MSE

- Train MSE includes synthetic augmentation (aug_ratio=0.5, noise injected to base action), inflating train loss vs val loss by ~1.5x
- perdof train_loss not directly captured; estimated from obs_only/scalar_unc train/val ratio pattern
- Mid-training snapshot (ep24) train_loss is higher than final convergence value; final train_loss would be lower

## Analysis

### 1. Training MSE correctly predicts closed-loop SR ranking

| Metric | obs_only | perdof | scalar |
|--------|:--------:|:------:|:------:|
| Val MSE rank | 1st (best) | 2nd | 3rd (worst) |
| Object SR rank | 1st (best) | 2nd | 3rd (worst) |
| Spatial SR rank | 1st (tied) | 1st (tied) | 3rd |

**The offline metric (val MSE) and online metric (closed-loop SR) are monotonically correlated.** There is NO disconnect between training loss and deployment success in this experiment. Lower MSE consistently maps to equal or higher SR.

### 2. The real story: conformal features HURT CRM training

| Comparison | Val MSE ratio | Object SR delta vs obs_only |
|------------|:---:|:---:|
| perdof vs obs_only | 2.17x worse | -8pp (11% vs 19%) |
| scalar vs obs_only | 2.27x worse | -10pp (9% vs 19%) |

The conformal features (per-DOF Mahalanobis components or scalar uncertainty) are noisy inputs that make the CRM harder to train. The obs_only model, which only uses the 960D observation embedding, learns a much better correction function.

### 3. CRM correction value depends on variant

| Comparison | Object SR delta | Spatial SR delta |
|------------|:-:|:-:|
| obs_only vs argmin | **+7pp** (19% vs 12%) | +1pp (35% vs 34%) |
| perdof vs argmin | **-1pp** (11% vs 12%) | +1pp (35% vs 34%) |
| scalar vs argmin | **-3pp** (9% vs 12%) | -2pp (32% vs 34%) |

Only obs_only CRM provides meaningful improvement over the argmin baseline. Perdof and scalar corrections **actively harm** performance on the Object benchmark (worse than simple sample selection with no correction).

### 4. Mechanism insight (paper narrative)

The "smoking gun" is NOT that "low MSE fails to predict SR" (it does predict it). The real insight is:

> **Per-DOF conformal features, despite their theoretical appeal for dimension-selective correction, produce noisier training signal (2.2x higher MSE) AND worse closed-loop performance. The observation embedding already encodes sufficient information for effective residual correction.**

This is a compelling negative result because:
1. The K=10 samples in 30D action space yield rank-deficient covariance, making per-dimension Mahalanobis components unreliable
2. Observation features (960D from the VLA backbone) implicitly encode task state including uncertainty-relevant information
3. Adding noisy conformal features as CRM input forces the network to learn to ignore them, consuming model capacity

### 5. Perdof magnitude collapse (supplementary evidence)

From magnitude sweep data (Object benchmark, seed 42):
- obs_only: stable across norms (0.1=19%, 0.2=22%, 0.3=19%, 1.42=17%)
- perdof: progressive collapse (0.1=11%, 0.2=11%, 0.3=4%, 1.42=0%)

The perdof model's corrections are directionally incorrect. At low norms, the damage is bounded. At high norms, the faulty direction is amplified, causing total failure. The obs_only model's corrections are directionally sound even without magnitude bounding.

## Summary

Training MSE and closed-loop SR are **correlated, not disconnected**. The key finding is that conformal features degrade both metrics simultaneously. This supports the paper's Narrative B: the correction mechanism itself (obs-conditioned CRM) is the contribution, not the specific uncertainty feature representation. Per-DOF conformal features are an honest negative result that strengthens the empirical analysis.
