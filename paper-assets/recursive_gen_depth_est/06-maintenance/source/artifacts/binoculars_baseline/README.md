# Binoculars Ordinal Depth Baseline

Binoculars (Hans et al., ICML 2024) baseline for ordinal generation-depth
estimation. Computes cross-perplexity ratio between observer and performer
LMs, then evaluates 4-class depth classification (d0-d3).

## Running

Full evaluation (all 9 cells, 5000 samples/depth):

```bash
CUDA_VISIBLE_DEVICES=0 python binoculars_ordinal_eval.py \
    --data_dir /root/autodl-tmp/recursive_gen_depth_est/data \
    --output_path /root/autodl-tmp/recursive_gen_depth_est/results/binoculars_baseline/binoculars_results.json \
    --gpu 0 \
    --batch_size 8
```

Quick debug run (100 samples/depth):

```bash
CUDA_VISIBLE_DEVICES=0 python binoculars_ordinal_eval.py \
    --data_dir /root/autodl-tmp/recursive_gen_depth_est/data \
    --output_path /root/autodl-tmp/recursive_gen_depth_est/results/binoculars_baseline/binoculars_debug.json \
    --gpu 0 \
    --max_samples 100 \
    --batch_size 16
```

Custom models:

```bash
python binoculars_ordinal_eval.py \
    --data_dir /root/autodl-tmp/recursive_gen_depth_est/data \
    --output_path ./results.json \
    --observer_model EleutherAI/pythia-1.4b \
    --performer_model EleutherAI/pythia-410m \
    --gpu 0
```

## Output format

```json
{
  "pythia_nucleus": {
    "equal_width":  {"4class_acc": 0.32, "4class_acc_std": 0.01, "d1d3_bal_acc": 0.33, "d1d3_bal_acc_std": 0.01},
    "coral":        {"4class_acc": 0.35, ...},
    "threshold":    {"4class_acc": 0.34, ...},
    "RF_single":    {"4class_acc": 0.36, ...},
    "RF_multi":     {"4class_acc": 0.40, ...}
  },
  "pythia_temp09": { ... },
  ...
  "__9cell_average__": {
    "equal_width":  {"4class_acc": ..., "d1d3_bal_acc": ...},
    ...
  },
  "__meta__": {
    "observer": "EleutherAI/pythia-1.4b",
    "performer": "EleutherAI/pythia-410m",
    "max_samples_per_depth": "all",
    "n_folds": 5,
    "rf_n_estimators": 200,
    "multi_features": ["bino_score", "ppl_mean", ...],
    "cell_times_sec": {"pythia_nucleus": 180.0, ...},
    "total_time_sec": 1620.0
  }
}
```

Per-cell `.npz` files are also saved alongside the JSON, containing raw
features and labels for downstream analysis.

## Evaluation methods

| Method | Features | Description |
|--------|----------|-------------|
| `equal_width` | 1 (score) | Divide score range into 4 equal bins; tries both directions |
| `coral` | 1 (score) | CORAL ordinal regression (cumulative logits) |
| `threshold` | 1 (score) | ROC-optimal thresholds at each depth boundary |
| `RF_single` | 1 (score) | RandomForest (200 trees) on raw Binoculars score |
| `RF_multi` | 11 | RandomForest (200 trees) on token-level statistics |

Multi-feature set (11 features derived from per-token values):
`bino_score, ppl_mean, ppl_var, ppl_median, ppl_p10, ppl_p90, ppl_skew,
xppl_mean, xppl_var, xppl_median, bino_score_median`

## Estimated GPU time

| Configuration | Samples | Time estimate |
|---------------|---------|---------------|
| Full (9 cells, 5000/depth) | 180,000 | ~30-60 min |
| Debug (9 cells, 100/depth) | 3,600 | ~3-5 min |

Estimates assume a single GPU (RTX 6000 Pro or similar). Models require
~3.6 GB VRAM (fp16); peak usage with logits ~5-6 GB at batch_size=8.

## Model choice

- Observer: `EleutherAI/pythia-1.4b` (matches our feature extraction reference model)
- Performer: `EleutherAI/pythia-410m` (smaller same-family model)

Both share the GPT-NeoX tokenizer (vocab_size=50304), which is required
for the cross-entropy computation between observer and performer distributions.

## Dependencies

All pre-installed in the project environment:
- torch, transformers (model inference)
- scikit-learn (RF, StratifiedKFold, metrics)
- numpy, tqdm
