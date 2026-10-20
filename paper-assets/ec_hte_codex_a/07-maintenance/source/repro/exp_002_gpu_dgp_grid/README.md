# exp_002_gpu_dgp_grid

Pending-only GPU DGP grid for H1.

This package prepares the planned Stage 0 grid but does not launch a formal job.
The formal run is gated on Director approval and GPU allocation.

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

## Dry run

```bash
cd /home/root/ec_hte
source /root/miniconda3/etc/profile.d/conda.sh
conda activate base
CUDA_VISIBLE_DEVICES=0 python repro/exp_002_gpu_dgp_grid/run_gpu_dgp_grid.py \
  --config configs/exp_002_gpu_dgp_grid.json \
  --output-dir artifacts/exp_002_gpu_dgp_grid/dry_run \
  --device cuda \
  --max-replications 2 \
  --limit-conditions 4 \
  --dry-run
```

## Required outputs

The script writes:

- `condition_metrics.jsonl`: condition-level metrics.
- `planned_metrics.json`: planned matrix metrics, each with `target_id`, `row`, `col`, `metric_key`, `exp_id`, and `source`.
- `summary.json`: run metadata, formal criteria, and output paths.

The mandatory controls are kept separate:

- `uncorrected`
- `oracle_global_confusion_correction`
- `estimated_global_confusion_correction`
- `stratified_subgroup_correction`

`estimated_global_confusion_correction` is reported separately from
`oracle_global_confusion_correction`.
