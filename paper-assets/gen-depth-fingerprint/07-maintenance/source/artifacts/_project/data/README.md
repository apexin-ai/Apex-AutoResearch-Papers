# Depth Profiling: Data Supplement

Data for reproducing the experiments in "Depth Profiling: Classifying Recursive Generation Depth in Base LLM Text Chains."

## Setup

```bash
pip install -r requirements.txt
```

A CUDA-capable GPU is required for feature extraction and generation steps.
A reference language model (e.g., Pythia-410M) must be available locally.

## Data Pipeline

### 1. Seed Preparation

Place Wikipedia seed texts in `data/wiki_seed_1000.jsonl` (each line: `{"id", "title", "text"}`).

### 2. Generation (depth-0 to depth-4 continuations)

```bash
python generate_chain.py \
    --input data/wiki_seed_1000.jsonl \
    --model-path /path/to/generator-model \
    --model-name pythia-2.8b \
    --output-dir data/ \
    --device cuda:0
```

Repeat for each generator model. Multi-GPU sharding is supported via `--shard-id` and `--num-shards`.

### 3. Feature Extraction

Extract 7 features (5 reference-model entropy features + 2 surface features) per text:

```bash
python extract_features.py \
    --input data/generations.jsonl \
    --output data/features.csv \
    --ref-model /path/to/pythia-410m \
    --device cuda:0
```

Alternative JSONL output format:

```bash
python extract_features_jsonl.py \
    --input data/generations.jsonl \
    --output data/features.jsonl \
    --ref-model /path/to/pythia-410m
```

### 4. Classification and Evaluation

Single-generator 3-class evaluation with Kruskal-Wallis tests:

```bash
python classify_and_eval.py --input data/features.csv --output results/mvp_results.json
```

## Evaluation Scripts

### Core LOGO Evaluation

8-generator Leave-One-Generator-Out (3-class and binary):

```bash
python eval_8gen_logo.py
```

### Ablation Studies

| Script | Description |
|--------|-------------|
| `eval_8gen_finer_depth.py` | 5-class vs 3-class depth granularity |
| `eval_8gen_sampling_ablation.py` | Training sample size ablation (25/50/75/100%) |
| `eval_8gen_cross_model_chains.py` | Cross-model chain extension evaluation |
| `scripts/lofo_ablation.py` | Leave-one-feature-out ablation |
| `scripts/alt_classifier_eval.py` | XGBoost vs LogisticRegression vs RandomForest |
| `scripts/bootstrap_ci_v2.py` | Bootstrap 95% confidence intervals |

### Robustness and Controls

| Script | Description |
|--------|-------------|
| `experiments/human_edit_robustness/run_robustness.py` | Word replacement robustness (0/5/10/20%) |
| `8gen_length_confound.py` | Length-matched confound control |
| `eval_8gen_baselines_pooled.py` | Pooled LOGO with detector baselines |
| `benchmark_efficiency.py` | Inference efficiency comparison |

### Dataset and Figures

| Script | Description |
|--------|-------------|
| `compute_dataset_stats.py` | Per-generator dataset statistics |
| `scripts/plot_fig1_strip.py` | Figure 1: per-generator Spearman rho strip plot |
| `scripts/plot_fig2.py` | Figure 2: LOGO grouped bar chart |
| `scripts/plot_fig3.py` | Figure 3: baseline comparison forest plot |

## Feature Descriptions

| Feature | Type | Description |
|---------|------|-------------|
| `entropy_mean` | Reference | Mean token-level entropy from reference model |
| `entropy_std` | Reference | Standard deviation of token-level entropy |
| `entropy_min` | Reference | Minimum token-level entropy |
| `entropy_max` | Reference | Maximum token-level entropy |
| `tail_decay` | Reference | Slope of sorted log-prob distribution (ranks 100-1000) |
| `ttr` | Surface | Type-token ratio |
| `hapax_ratio` | Surface | Proportion of words appearing exactly once |
