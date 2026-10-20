# exp_003_stage1_correction_ablation Proposal

- plan_id: `plan_003_stage1_correction_ablation`
- exp_id: `exp_003_stage1_correction_ablation`
- deps: `plan_001_h1_cpu_mvp` DONE(success); `plan_002_h1_gpu_dgp_grid` must be DONE before formal launch
- status: code/config/proposal prepared only; no formal experiment submitted

## Objective

Test H2: at low expert-label budget, hierarchical/partial-pooling subgroup confusion correction should improve primary `gate_rmse` versus global correction while remaining non-inferior to per-subgroup independent correction.

## Methods

- `global`
- `arm_specific`
- `per_subgroup_independent`
- `partial_pooling`

## Budgets

- low: `B=100`
- mid: `B=500`

Formal config uses `N in {2000, 5000}`, `k in {3, 6}`, high misclassification heterogeneity, high CATE heterogeneity, positive and negative correlation controls, and `R=200` replications per condition.

## Operational Criteria

Primary metric: `gate_rmse`.

Success gate:

- `partial_pooling_minus_global` bootstrap 95% CI upper bound `< 0`
- relative non-inferiority against `per_subgroup_independent` within 5% GATE RMSE margin

Secondary diagnostics:

- `pehe`
- `mean_subgroup_cate_bias`

## Provenance Contract

Every matrix row written by the script includes:

- `target_id`
- `row`
- `col`
- `metric_key`
- `exp_id`
- `source`

Targets:

- `C_PARTIAL_POOLING_BETTER_LOW_BUDGET`
- `T_STAGE1_CORRECTION_ABLATION`

## Commands

Help:

```bash
python3 repro/exp_003_stage1_correction_ablation/run_stage1_ablation.py --help
```

Tiny smoke only:

```bash
python3 repro/exp_003_stage1_correction_ablation/run_stage1_ablation.py \
  --config configs/exp_003_stage1_correction_ablation.json \
  --output-dir artifacts/exp_003_stage1_correction_ablation/smoke \
  --smoke \
  --max-replications 2 \
  --limit-conditions 2
```

Formal command placeholder after exp002 completion and approval:

```bash
python3 repro/exp_003_stage1_correction_ablation/run_stage1_ablation.py \
  --config configs/exp_003_stage1_correction_ablation.json \
  --output-dir artifacts/exp_003_stage1_correction_ablation/formal \
  --allow-formal \
  --confirm-exp002-done
```
