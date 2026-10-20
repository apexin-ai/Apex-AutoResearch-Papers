# Generation Depth Fingerprinting: Code Supplement

Code for reproducing the experiments in "Generation Depth Fingerprinting."

## Requirements

- Python 3.10+
- CUDA-capable GPU (for generation, feature extraction, and end-to-end classifier)
- A reference language model (e.g., EleutherAI/pythia-410m) available locally or via HuggingFace Hub

Install dependencies:

```bash
pip install -r requirements.txt
```

## Directory Structure

`code/` and `data/` are sibling directories under the supplement root. All scripts assume they are run from the `code/` directory and access data via `../data/`.

```
supplement/
├── code/          # Scripts (this directory)
│   ├── README.md
│   ├── generate_chain.py
│   ├── scripts/
│   └── experiments/
└── data/          # Data files (not included due to size; see data/README.md for format)
    ├── README.md
    ├── features_all_models.csv
    └── ...
```

## Data Format

**Features CSV** (`features_all_models.csv`): One row per text sample with columns:

| Column | Description |
|--------|-------------|
| `model_name` | Generator model identifier (e.g., `pythia-2.8b`) |
| `seed_id` | Wikipedia seed text identifier |
| `depth` | Generation depth (0 = human, 1 = first-gen, 2+ = deeper) |
| `entropy_mean` | Mean token-level entropy from reference model |
| `entropy_std` | Std dev of token-level entropy |
| `entropy_min` | Minimum token-level entropy |
| `entropy_max` | Maximum token-level entropy |
| `tail_decay` | Slope of sorted log-prob distribution (ranks 100-1000) |
| `ttr` | Type-token ratio |
| `hapax_ratio` | Proportion of words appearing exactly once |

**Generations JSONL**: One JSON object per line with fields `{"seed_id", "depth", "text", "model_name"}`.

## Reproduction Steps

### 1. Generate continuation chains (depth 0 to 4)

```bash
python generate_chain.py \
    --input ../data/wiki_seed_1000.jsonl \
    --model-path /path/to/generator-model \
    --model-name pythia-2.8b \
    --output-dir ../data/ \
    --device cuda:0
```

Repeat for each generator model. Multi-GPU sharding is supported via `--shard-id` and `--num-shards`.

### 2. Extract features

Extract 7 features (5 reference-model entropy features + 2 surface features) per text:

```bash
python extract_features.py \
    --input ../data/generations.jsonl \
    --output ../data/features.csv \
    --ref-model /path/to/pythia-410m \
    --device cuda:0
```

Alternative JSONL output: use `extract_features_jsonl.py` with the same arguments.

### 3. Train classifier and evaluate

Single-generator 3-class evaluation with Kruskal-Wallis tests:

```bash
python classify_and_eval.py --input ../data/features.csv --output results/mvp_results.json
```

### 4. LOGO evaluation (main results)

8-generator Leave-One-Generator-Out evaluation (3-class and binary):

```bash
python eval_8gen_logo.py
```

## Script Reference

### Core Pipeline

| Script | Description |
|--------|-------------|
| `generate_chain.py` | Generate depth-0 to depth-4 continuation chains |
| `extract_features.py` | Extract 7 features from text (CSV output) |
| `extract_features_jsonl.py` | Extract 7 features from text (JSONL output) |
| `classify_and_eval.py` | XGBoost 3-class classification with statistical tests |
| `eval_8gen_logo.py` | 8-generator LOGO evaluation (main paper results) |

### Ablation and Analysis

| Script | Description |
|--------|-------------|
| `eval_8gen_finer_depth.py` | 5-class vs 3-class depth granularity (Appendix D) |
| `eval_8gen_sampling_ablation.py` | Training sample size ablation at 25/50/75/100% (Appendix H) |
| `eval_8gen_cross_model_chains.py` | Cross-model chain extension evaluation (Appendix M) |
| `eval_8gen_baselines_pooled.py` | Pooled LOGO with detector baselines (main paper) |
| `cross_temp_transfer.py` | Cross-temperature transfer evaluation (Appendix O) |
| `end_to_end_classifier.py` | QLoRA end-to-end depth classification (Appendix E) |
| `distributional_tests.py` | KS + Levene distributional tests on features (Appendix N) |
| `scripts/lofo_ablation.py` | Leave-one-feature-out ablation (Appendix F) |
| `scripts/alt_classifier_eval.py` | XGBoost vs LogisticRegression vs RandomForest (Appendix H) |
| `scripts/bootstrap_ci_v2.py` | Bootstrap 95% confidence intervals |
| `scripts/tost_equivalence.py` | TOST equivalence testing for downstream results (Appendix L) |

### Robustness and Controls

| Script | Description |
|--------|-------------|
| `experiments/human_edit_robustness/run_robustness.py` | Word replacement robustness at 0/5/10/20% (Appendix I) |
| `8gen_length_confound.py` | Length-matched confound control (Appendix B) |
| `benchmark_efficiency.py` | Inference efficiency comparison |

### Downstream Utility (Appendix L)

| Script | Description |
|--------|-------------|
| `prepare_downstream_data.py` | Build depth-stratified training data variants |
| `finetune_downstream.py` | Fine-tune causal LM on each variant, measure perplexity |
| `bootstrap_downstream_ci.py` | Bootstrap CI and effect sizes for downstream results |

### Dataset Statistics and Figures

| Script | Description |
|--------|-------------|
| `compute_dataset_stats.py` | Per-generator dataset statistics (Appendix A) |
| `scripts/plot_fig1_strip.py` | Figure 1: per-generator Spearman rho strip plot |
| `scripts/plot_fig2.py` | Figure 2: LOGO grouped bar chart |
| `scripts/plot_fig3.py` | Figure 3: baseline comparison forest plot |
