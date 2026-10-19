# Plan 005: Stratified Analysis Specification

## Pipeline

Three-stage pipeline, stages 1 & 3 are CPU-only:

1. **`prepare_stratification_index.py`** (CPU, DONE) — parses all.jsonl → `stratification_index.json`
2. **`evaluate_stratified.py`** (GPU, awaiting M2 checkpoints) — per-query eval with pool_size control
3. **`analyze_stratified.py`** (CPU) — stratification + bootstrap CI + plots

## 5 Stratification Dimensions

| # | Dimension | Bins | Source | Method |
|---|-----------|------|--------|--------|
| 1 | Repo size (file count) | small (<50), medium (50-200), large (200+) | `stratification_index.json` → `repo_file_count` | Fixed thresholds (matches BM25 overlap analysis) |
| 2 | Eval pool size | Quartiles | Per-query eval output → `pool_size` | Data-driven quartiles |
| 3 | Query-positive similarity | Quartiles | Per-query eval output → `query_pos_sim` | Data-driven quartiles |
| 4 | Structural data availability | Binary: with_structural / no_structural | `stratification_index.json` → `has_structural` | Binary (34.3% with / 65.7% without) |
| 5 | Negative difficulty | Quartiles of mean neg cosine sim | Per-query eval output → `mean_neg_sim` | Data-driven quartiles |

## Pool Size Control (D038)

`evaluate_stratified.py` accepts `--pool-sizes 50,100,200,500` to test strategy ranking stability across pool sizes. Each pool size produces a separate per-query JSONL. Analysis is run independently per pool size.

Padding strategy: when a query has fewer candidates than target pool_size, pad with global distractors from other queries in the same val set (same as `eval_p2b_pooled.py`).

## Data Sources

- **M1 metadata**: `/root/autodl-tmp/structfuse/stratification_index.json` (19MB, 44,173 instances, 123 repos)
- **Val data**: `/root/autodl-tmp/structfuse/full_m2_training_data/val_{strategy}_s{seed}.jsonl` (2,980 queries each)
- **Checkpoints**: `/root/autodl-tmp/structfuse/checkpoints/m2_full_{encoder}/{strategy}_s{seed}/`

## Per-query Output Schema

```json
{
  "query_id": "instance_id::file_path",
  "instance_id": "repo.commit.mutation__hash",
  "gold_rank": 0,
  "pool_size": 50,
  "query_pos_sim": 0.712345,
  "mean_neg_sim": 0.351234,
  "max_neg_sim": 0.581234,
  "hit_at_1": true,
  "hit_at_5": true,
  "hit_at_10": true
}
```

## Analysis Outputs

- `stratified_results.json` — full results with bootstrap 95% CIs per stratum
- `stratified_results.csv` — flat table for easy import
- `stratified_{dimension}.pdf` — bar charts: R@1 per strategy (left), delta vs random (right)
- Weighted aggregate delta per dimension (accounts for stratum sizes)

## Execution Plan

When M2 checkpoints are ready:

```bash
# Stage 2: per-query eval (GPU, ~30min per run × 18 runs)
for encoder in qwen starcoder; do
  for strategy in random embedding_distance dataflow_aware; do
    for seed in 42 43 44; do
      python evaluate_stratified.py \
        --ckpt-dir /root/autodl-tmp/structfuse/checkpoints/m2_full_${encoder}/${strategy}_s${seed} \
        --model-name /root/autodl-tmp/structfuse/models/${model_path} \
        --val-file /root/autodl-tmp/structfuse/full_m2_training_data/val_${strategy}_s${seed}.jsonl \
        --pool-sizes 50 \
        --output-dir /root/structfuse/results/stratified/per_query \
        --tag ${encoder}_${strategy}_s${seed}
    done
  done
done

# Stage 3: analysis (CPU, <1min)
python analyze_stratified.py \
  --results-dir /root/structfuse/results/stratified/per_query \
  --index-file /root/autodl-tmp/structfuse/stratification_index.json \
  --strategies random,embedding_distance,dataflow_aware \
  --encoder qwen --seeds 42,43,44 --pool-size 50 \
  --output-dir /root/structfuse/results/stratified
```

## Verification

- [x] `prepare_stratification_index.py` — completed, 44,173 instances indexed
- [x] `evaluate_stratified.py --dry-run` — passed (2,980 queries, multi-pool-size)
- [x] `analyze_stratified.py --dry-run` — passed (5 dimensions, JSON+CSV+5 PDFs)
- [ ] Real eval — awaiting M2 checkpoints
