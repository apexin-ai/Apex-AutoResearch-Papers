# Meta-Brain Phase 0: Perturbation Classifier on π₀ Activations

Validates whether frozen π₀ internal activations contain sufficient signal to distinguish perturbation types in LIBERO-Plus — a prerequisite for downstream LoRA routing.

## Pipeline

```
collect_activations.py → train_classifier.py → eval_classifier.py
```

### 1. Collect activations

```bash
# All 6 perturbation types (50 episodes each)
python collect_activations.py \
    --checkpoint /path/to/pi0_base \
    --output_dir ./activations \
    --perturbation_type all \
    --num_episodes 50 \
    --device cuda:0

# Nominal baseline (100 episodes)
python collect_activations.py \
    --checkpoint /path/to/pi0_base \
    --output_dir ./activations \
    --perturbation_type nominal \
    --num_episodes 100
```

Output: `activations/{camera_viewpoints,light_conditions,...,nominal}.pt`

Each `.pt` file is a list of dicts with keys:
- `activations`: `{layer_name: {pooling_type: tensor(fp16)}}`
- `label_6class`, `label_3class`, `label_binary`: int labels
- `metadata`: episode info (task, steps, success)

Incremental: run collection per perturbation type across sessions — files append automatically.

### 2. Train classifier

```bash
# Single config
python train_classifier.py \
    --data_dir ./activations \
    --mode 6class \
    --activation_source both \
    --pooling mean \
    --lr 1e-3 \
    --output_dir ./models

# Full sweep (27 configs: 3 pooling × 3 source × 3 lr)
python train_classifier.py \
    --data_dir ./activations \
    --mode 6class \
    --sweep \
    --output_dir ./models
```

Each config saves `best_model.pt` + `result.json` under `models/<config_name>/`.

### 3. Evaluate

```bash
# Single model
python eval_classifier.py \
    --model_path ./models/6class__mean__both__lr0.001/best_model.pt \
    --data_dir ./activations \
    --mode 6class \
    --activation_source both \
    --pooling mean \
    --output_dir ./eval_results

# Per-layer breakdown (which layers carry the most signal)
python eval_classifier.py \
    --model_path ./models/6class__mean__both__lr0.001/best_model.pt \
    --data_dir ./activations \
    --mode 6class \
    --activation_source both \
    --pooling mean \
    --per_layer \
    --output_dir ./eval_results

# Sweep leaderboard
python eval_classifier.py \
    --sweep_results_dir ./models \
    --mode 6class \
    --output_dir ./eval_results
```

Outputs:
- `classification_report.txt` — per-class precision/recall/F1
- `confusion_matrix.png` + `.csv` — normalized confusion matrix
- `roc_curve.png` + `pr_curve.png` — (binary mode only)
- `tsne.png` — activation space visualization
- `per_layer_accuracy.png` + `.json` — layer-level informativeness
- `sweep_leaderboard_{mode}.csv` — all configs ranked by accuracy

## Architecture

**π₀ hooks** (12 layers total):
- PaliGemma LLM: layers {2,4,6,8,10,12,14,16} — hidden_dim=2048
- Action Expert: layers {2,6,10,14} — hidden_dim=1024

**Classifier**: 2-layer MLP, hidden_dim=256, dropout=0.3

**Input dimensions** (with mean/first/last pooling):
- `paligemma_only`: 8×2048 = 16,384
- `expert_only`: 4×1024 = 4,096
- `both`: 20,480

With `first_last` pooling, dimensions double.

## Perturbation Taxonomy

| 6-class | 3-class | Binary |
|---------|---------|--------|
| camera_viewpoints | visual (0) | perturbed (1) |
| light_conditions | visual (0) | perturbed (1) |
| background_textures | visual (0) | perturbed (1) |
| sensor_noise | visual (0) | perturbed (1) |
| objects_layout | spatial (1) | perturbed (1) |
| robot_initial_states | physical (2) | perturbed (1) |
| *(nominal)* | — | nominal (0) |

## Go/No-Go Thresholds

| Mode | Minimum Accuracy | Notes |
|------|-----------------|-------|
| 6-class | 50% | chance = 16.7% |
| 3-class | 65% | chance = 33.3% |
| Binary | 80% accuracy, 0.85 AUC | chance = 50% |

## Dependencies

```
torch
safetensors
scikit-learn
matplotlib
numpy
openpi          # π₀ model loading
libero          # LIBERO-Plus environment
```

Optional: `umap-learn` for UMAP visualization.
