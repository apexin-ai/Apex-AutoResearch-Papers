# exp_002_gpu_dgp_grid Pending Proposal

Status target: PENDING only. Formal GPU execution is blocked until Director
approval and allocation.

## Hypothesis

Positive misclassification-CATE correlation makes a single pooled global
confusion correction structurally worse than uncorrected subgroup estimates,
because the global correction under-corrects high-error/high-CATE subgroups and
over-corrects low-error/low-CATE subgroups. Negative-correlation controls should
show a materially lower oracle-global-worse rate.

Parent: null

## Formal command

```bash
cd /home/root/ec_hte
source /root/miniconda3/etc/profile.d/conda.sh
conda activate base
CUDA_VISIBLE_DEVICES=0 python repro/exp_002_gpu_dgp_grid/run_gpu_dgp_grid.py \
  --config configs/exp_002_gpu_dgp_grid.json \
  --output-dir artifacts/exp_002_gpu_dgp_grid/formal \
  --device cuda
```

## Runtime environment

- server: seetacloud-38274
- account: root
- gpu_ids: cuda:0
- GPU: NVIDIA RTX PRO 6000 Blackwell Server Edition, 97887 MiB
- driver: 580.82.09
- CUDA: torch CUDA 12.8
- torch: 2.8.0+cu128
- Python: 3.12.3 in `/root/miniconda3` base
- project_root: `/home/root/ec_hte`

## Data and count

- data_path: synthetic DGP generated in-run; no external input dataset
- data_count: 96 planned conditions x 200 replications per condition = 19200
  replications
- model_name: synthetic_torch_dgp_grid_no_trained_model
- seed: 20260531

## Disk/runtime estimates

- disk estimate: <250 MB for JSONL/JSON summaries; no model checkpoint download
- expected runtime: <=2 GPU-hours on `seetacloud-38274/root/cuda:0`

## Output paths

- log_path: `/home/root/ec_hte/artifacts/exp_002_gpu_dgp_grid/logs/exp_002_gpu_dgp_grid_<timestamp>.log`
- checkpoint_path: `/home/root/ec_hte/artifacts/exp_002_gpu_dgp_grid/checkpoints/no_model_checkpoint_required.txt`
- artifact_path: `/home/root/ec_hte/artifacts/exp_002_gpu_dgp_grid/formal/`
- dry_run_path: `/home/root/ec_hte/artifacts/exp_002_gpu_dgp_grid/dry_run/`

## Grid hyperparameters

- N: [2000, 5000, 10000]
- subgroup counts k: [3, 6]
- expert budgets B: [100, 500, 1000, 2000]
- misclassification heterogeneity: [low, high]
- CATE heterogeneity: [low, high]
- correlation directions: [positive, negative]
- replications_per_condition: 200
- bootstrap_iterations: 1000
- treatment_probability: 0.5
- noise_sd: 1.0
- controls: uncorrected, oracle_global_confusion_correction,
  estimated_global_confusion_correction, stratified_subgroup_correction

Estimated-global is reported separately from oracle-global in all planned
outputs.

## Operational criteria

- primary_metric: global_worse_rate_difference_positive_minus_negative
- success_rule: positive-correlation conditions have oracle-global-worse rate at
  least 20 percentage points higher than negative-correlation controls, with
  bootstrap 95% CI lower bound > 0
- bias-bound diagnostic: Spearman rho >= 0.50 with bootstrap 95% CI lower bound
  > 0
- secondary_metrics: bias_bound_vs_global_worse_spearman,
  estimated_global_minus_oracle_global_gate_rmse
- minimum replications: 200 per condition

## Matrix target mapping

All planned metric outputs must carry `target_id,row,col,metric_key,exp_id,source`.

| target_id | row | col | metric_key | exp_id | source |
|---|---|---|---|---|---|
| C_H1_GLOBAL_CORRECTION_WORSE | exp_002_gpu_dgp_grid | grid_oracle_vs_estimated_mechanism_split | bias_bound_predicts_global_worse_rate_by_correction_type | exp_002_gpu_dgp_grid | `/home/root/ec_hte/artifacts/exp_002_gpu_dgp_grid/formal/condition_metrics.jsonl` |
| T_STAGE0_DGP_GRID | grid_all_conditions | bias_bound_auc_or_rank_corr | bias_bound_vs_global_worse_rank_corr | exp_002_gpu_dgp_grid | `/home/root/ec_hte/artifacts/exp_002_gpu_dgp_grid/formal/condition_metrics.jsonl` |
| T_STAGE0_DGP_GRID | grid_all_conditions | oracle_estimated_gap | estimated_global_minus_oracle_global_gate_rmse | exp_002_gpu_dgp_grid | `/home/root/ec_hte/artifacts/exp_002_gpu_dgp_grid/formal/condition_metrics.jsonl` |

## Pending-only guard

No `submit_training_job`, no `tmux`, no `nohup`, no QUEUED/ALLOCATED/RUNNING
transition is permitted during this preparation step.
