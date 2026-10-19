# Generated Summaries

This directory is the default destination for locally generated tables, figures,
and audit reports. Generated files are intentionally ignored by Git. Each artifact
should document its source run tags, seeds, metric direction, and validation
status.

Large checkpoints, task work directories, caches, raw logs, and derived summaries
are intentionally excluded from the repository.

## Multiseed Artifacts

Run `analysis/summarize_multiseed.py` to create `results/summary/multiseed/`.
The generated files have distinct roles:

- `multiseed_paper_table.csv`: the final-step category and overall values in
  Supplementary Table 5;
- `multiseed_method_summary.csv`: one row per method, including the formal
  seed-first aggregate and explicitly named raw-mean-first diagnostics;
- `multiseed_per_task.csv`: scored task-by-seed values and task-level
  summaries;
- `multiseed_category_summary.csv`: category-level seed-first summaries;
- `multiseed_per_run.csv`: strict provenance and protocol audit for every
  method, seed, and task;
- `multiseed_repair_plan.csv`: only missing or invalid runs, suitable for
  targeted reruns;
- `multiseed_summary.json`: complete machine-readable aggregate;
- `multiseed_summary.md`: compact reader-facing status and result table.

The formal aggregation order is to score every task and seed first, aggregate
tasks within each seed, and then average the seed-level summaries. Averaging
raw task metrics across seeds before scoring is retained only as a diagnostic
because clipping, thresholding, and anchor attainment make the two orders
non-equivalent.

## Statistical Robustness Artifacts

Run `analysis/compute_statistical_robustness.py` after the multiseed summary
and best-so-far detail files are available. It creates
`results/summary/statistical_robustness/`:

- `final_step_bootstrap.csv`: Supplementary Table 6;
- `best_so_far_bootstrap.csv` and `seed_level_summary.csv`: Supplementary
  Table 8;
- `paired_differences.csv`: Supplementary Table 9;
- `latex_rows.tex`: the rounded rows used to cross-check those tables.

Formal comparisons should use only methods marked `protocol_valid`. A run is
valid only when it contains the baseline plus five completed interventions,
five decisions, a usable final metric, the requested replicate seed, and zero
top-level or nested fallback decisions.
