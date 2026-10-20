# exp_001_bias_bound_mvp

- exp_id: exp_001_bias_bound_mvp
- DGP: positive_corr_high_high
- primary_metric: gate_rmse
- n_replications: 10
- n_per_replication: 4000
- expert_budget: 600
- tau_values: [0.0, 4.3, 5.4, 5.5]
- error_rates: [0.02, 0.06, 0.29, 0.45]
- group_probs: [0.59, 0.09, 0.14, 0.18]

## Primary result

`oracle_global - uncorrected` gate_rmse = 0.650634 [0.564392, 0.714418]
Conclusion: success

## Estimated global noise

`estimated_global - oracle_global` gate_rmse = 0.031970 [-0.034895, 0.117762]

## Method gate_rmse

- uncorrected: 0.274640 [0.245257, 0.299009]
- oracle_global_confusion_correction: 0.925274 [0.849169, 1.000448]
- estimated_global_confusion_correction: 0.957244 [0.863016, 1.068268]
- stratified_subgroup_correction: 0.153284 [0.124334, 0.182985]

## Secondary diagnostics

- oracle_global_minus_uncorrected_mean_subgroup_cate_bias: 0.548273 [0.478698, 0.609820]
- oracle_global_minus_uncorrected_max_subgroup_cate_bias: 1.049987 [0.907638, 1.175455]

## Matrix rows

- C_H1_GLOBAL_CORRECTION_WORSE / exp_001_bias_bound_mvp / uncorrected_vs_oracle_global / oracle_global_minus_uncorrected_gate_rmse = 0.650634
- C_H1_GLOBAL_CORRECTION_WORSE / exp_001_bias_bound_mvp / uncorrected_vs_estimated_global / estimated_global_minus_uncorrected_gate_rmse = 0.682603
- T_STAGE0_DGP_GRID / positive_corr_high_mis_high_cate / uncorrected_gate_rmse / positive_corr_high_high.uncorrected_gate_rmse = 0.274640
- T_STAGE0_DGP_GRID / positive_corr_high_mis_high_cate / oracle_global_gate_rmse / positive_corr_high_high.oracle_global_gate_rmse = 0.925274
- T_STAGE0_DGP_GRID / positive_corr_high_mis_high_cate / estimated_global_gate_rmse / positive_corr_high_high.estimated_global_gate_rmse = 0.957244
- T_STAGE0_DGP_GRID / positive_corr_high_mis_high_cate / stratified_gate_rmse / positive_corr_high_high.stratified_gate_rmse = 0.153284
