# Training Dynamics Analysis

## Key Findings
- **Loss curves**: Three methods nearly identical unweighted loss (~2.09 final), very noisy (batch_size=4)
- **b* distribution**: Stable throughout training. Median ~0.85, mean ~1.35 (right-skewed), P25 ~0.54, P75 ~1.50. No drift.
- **alpha_eff binding rate**: Stable at ~40%, no trend. ~40% batches have alpha_eff as binding constraint.

## Files (artifacts/dynamics/)
- training_dynamics_data.json (120 loss points + 62 b*/alpha windows)
- fig_loss_curves.py/.pdf/.png
- fig_bstar_trajectory.py/.pdf/.png
- fig_alpha_eff_binding.py/.pdf/.png