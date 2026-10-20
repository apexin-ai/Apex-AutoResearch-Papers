# exp_001 H1 findings update points

## Audit verdict

- Usable for technical report: yes, as an H1 CPU MVP / single-DGP result.
- Registry status: `DONE(success)`.
- Primary metric: `gate_rmse`.
- Consistency check: registry metrics, `artifacts/exp_001_bias_bound_mvp/formal/summary.json`, `artifacts/exp_001_bias_bound_mvp/formal/matrix_metrics.jsonl`, registered data copies, and `experiment_matrix.yaml` agree for all exp_001 filled cells.
- CI rule: `oracle_global_minus_uncorrected_gate_rmse` 95% bootstrap CI lower bound is > 0.
- Estimated-global handling: report separately from oracle-global; do not conflate structural oracle-global degradation with finite-sample confusion-estimation noise.
- Secondary diagnostics: same direction; `mixed=false`.

## Provenance rows

| target_id | row | col | metric_key | exp_id | source |
|---|---|---|---|---|---|
| C_H1_GLOBAL_CORRECTION_WORSE | exp_001_bias_bound_mvp | uncorrected_vs_oracle_global | oracle_global_minus_uncorrected_gate_rmse | exp_001_bias_bound_mvp | repro/exp_001_bias_bound_mvp/run_experiment.py::artifacts/exp_001_bias_bound_mvp/formal |
| C_H1_GLOBAL_CORRECTION_WORSE | exp_001_bias_bound_mvp | uncorrected_vs_estimated_global | estimated_global_minus_uncorrected_gate_rmse | exp_001_bias_bound_mvp | repro/exp_001_bias_bound_mvp/run_experiment.py::artifacts/exp_001_bias_bound_mvp/formal |
| T_STAGE0_DGP_GRID | positive_corr_high_mis_high_cate | uncorrected_gate_rmse | positive_corr_high_high.uncorrected_gate_rmse | exp_001_bias_bound_mvp | repro/exp_001_bias_bound_mvp/run_experiment.py::artifacts/exp_001_bias_bound_mvp/formal |
| T_STAGE0_DGP_GRID | positive_corr_high_mis_high_cate | oracle_global_gate_rmse | positive_corr_high_high.oracle_global_gate_rmse | exp_001_bias_bound_mvp | repro/exp_001_bias_bound_mvp/run_experiment.py::artifacts/exp_001_bias_bound_mvp/formal |
| T_STAGE0_DGP_GRID | positive_corr_high_mis_high_cate | estimated_global_gate_rmse | positive_corr_high_high.estimated_global_gate_rmse | exp_001_bias_bound_mvp | repro/exp_001_bias_bound_mvp/run_experiment.py::artifacts/exp_001_bias_bound_mvp/formal |
| T_STAGE0_DGP_GRID | positive_corr_high_mis_high_cate | stratified_gate_rmse | positive_corr_high_high.stratified_gate_rmse | exp_001_bias_bound_mvp | repro/exp_001_bias_bound_mvp/run_experiment.py::artifacts/exp_001_bias_bound_mvp/formal |

## Key numbers

- DGP/config: `positive_corr_high_high`; `n_replications=200`, `n=10000`, `expert_budget=600`, bootstrap replications `2000`.
- Uncorrected GATE RMSE: 0.26032738576584474; 95% CI [0.25639859614257954, 0.26408682391063765].
- Oracle global GATE RMSE: 0.9250125318322816; 95% CI [0.9182077046539118, 0.9317305615892383].
- Estimated global GATE RMSE: 0.9431012510287877; 95% CI [0.9282465338704898, 0.9588437571646938].
- Stratified subgroup GATE RMSE: 0.08234754252792217; 95% CI [0.07761227706803817, 0.0871652592079366].

## Primary comparison

- `oracle_global_minus_uncorrected_gate_rmse`: 0.6646851460664368; 95% CI [0.6574673897400952, 0.6717956725076197].
- Relative to uncorrected, oracle global increases GATE RMSE by 255.3266319296494%; oracle global is 3.553266319296494x the uncorrected RMSE.
- This supports H1 for the primary metric under this positive-correlation high-misclassification/high-CATE-heterogeneity MVP setting.

## Estimated-global separate report

- `estimated_global_minus_uncorrected_gate_rmse`: 0.682773865262943; 95% CI [0.66743837339491, 0.6982090441249844].
- Relative to uncorrected, estimated global increases GATE RMSE by 262.2750822985154%; estimated global is 3.622750822985154x the uncorrected RMSE.
- `estimated_global_minus_oracle_global_gate_rmse`: 0.018088719196506182; 95% CI [0.005477944594796951, 0.03140296703176313].
- Estimated-vs-oracle gap is 0.018088719196506182 absolute, equal to 1.955510717317057% of oracle-global GATE RMSE.

## Secondary diagnostics

- `oracle_global_minus_uncorrected_mean_subgroup_cate_bias`: 0.550346749960143; 95% CI [0.5429471054744693, 0.55716582317215].
- `oracle_global_minus_uncorrected_max_subgroup_cate_bias`: 1.086059985068446; 95% CI [1.069359619458318, 1.1021949609964543].
- Both diagnostics point in the same direction as the primary metric; `opposite_secondary_diagnostics=[]`; `mixed=false`.

## Suggested Director edits for findings.md

- Write: H1 CPU MVP supports the claim that pooled oracle global confusion correction can be worse than uncorrected noisy annotations when subgroup misclassification and CATE heterogeneity are positively aligned. Use only `gate_rmse` as the primary metric.
- Write: The main reportable estimate is oracle global minus uncorrected GATE RMSE = 0.664685, 95% bootstrap CI [0.657467, 0.671796], CI lower > 0.
- Write: Uncorrected, oracle global, estimated global, and stratified GATE RMSE are respectively 0.260327, 0.925013, 0.943101, and 0.082348. Oracle global is 3.553x uncorrected; estimated global is 3.623x uncorrected.
- Write: Estimated-global results should be reported as a separate finite-sample confusion-estimation result: estimated-global minus oracle-global GATE RMSE = 0.018089, 95% CI [0.005478, 0.031403].
- Write: Secondary diagnostics are aligned with the primary result: mean subgroup CATE bias difference = 0.550347 and max subgroup CATE bias difference = 1.086060; no mixed diagnostic flag.
- Retain: any statement that exp_001 is a Stage 0 / CPU MVP / single positive_corr_high_high DGP mechanism check rather than a full grid robustness result.
- Retain: the need for exp_002 GPU DGP grid before making broad claims over correlation directions, budgets, group counts, and heterogeneity regimes.
- Revoke or avoid: any wording that says estimated global is the primary evidence for H1, or that does not separate oracle-global structural bias from estimated-global finite-sample noise.
- Revoke or avoid: any claim that H1 is fully established across all DGP settings; exp_001 only validates the intended mechanism in the formal MVP condition.
- Revoke or avoid: any statement implying secondary diagnostics are mixed or contradict the primary metric.
