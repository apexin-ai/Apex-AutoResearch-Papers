# exp_001_bias_bound_mvp

- exp_id: exp_001_bias_bound_mvp
- DGP: positive_corr_high_high
- primary_metric: gate_rmse
- n_replications: 200
- n_per_replication: 10000
- expert_budget: 600
- tau_values: [0.0, 4.3, 5.4, 5.5]
- error_rates: [0.02, 0.06, 0.29, 0.45]
- group_probs: [0.59, 0.09, 0.14, 0.18]

## Primary result

`oracle_global - uncorrected` gate_rmse = 0.664685 [0.657467, 0.671796]
Conclusion: success

## Estimated global noise

`estimated_global - oracle_global` gate_rmse = 0.018089 [0.005478, 0.031403]

## Method gate_rmse

- uncorrected: 0.260327 [0.256399, 0.264087]
- oracle_global_confusion_correction: 0.925013 [0.918208, 0.931731]
- estimated_global_confusion_correction: 0.943101 [0.928247, 0.958844]
- stratified_subgroup_correction: 0.082348 [0.077612, 0.087165]

## Secondary diagnostics

- oracle_global_minus_uncorrected_mean_subgroup_cate_bias: 0.550347 [0.542947, 0.557166]
- oracle_global_minus_uncorrected_max_subgroup_cate_bias: 1.086060 [1.069360, 1.102195]

## Matrix rows

- C_H1_GLOBAL_CORRECTION_WORSE / exp_001_bias_bound_mvp / uncorrected_vs_oracle_global / oracle_global_minus_uncorrected_gate_rmse = 0.664685
- C_H1_GLOBAL_CORRECTION_WORSE / exp_001_bias_bound_mvp / uncorrected_vs_estimated_global / estimated_global_minus_uncorrected_gate_rmse = 0.682774
- T_STAGE0_DGP_GRID / positive_corr_high_mis_high_cate / uncorrected_gate_rmse / positive_corr_high_high.uncorrected_gate_rmse = 0.260327
- T_STAGE0_DGP_GRID / positive_corr_high_mis_high_cate / oracle_global_gate_rmse / positive_corr_high_high.oracle_global_gate_rmse = 0.925013
- T_STAGE0_DGP_GRID / positive_corr_high_mis_high_cate / estimated_global_gate_rmse / positive_corr_high_high.estimated_global_gate_rmse = 0.943101
- T_STAGE0_DGP_GRID / positive_corr_high_mis_high_cate / stratified_gate_rmse / positive_corr_high_high.stratified_gate_rmse = 0.082348
