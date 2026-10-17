# Schema-DAG-Extraction

Code for "Schema-Induced Degradation in Training-Free LLM Information Extraction" (anonymous submission).

## Setup

```bash
pip install -r requirements.txt
```

We use **Qwen3-32B** served via vLLM v0.20.2 for all extraction experiments.

## Data

See `data/README.md` for dataset download instructions. We evaluate on four IE benchmarks:
- **Few-NERD** (NER, 66 entity types)
- **FewRel** (RE, 80 relation types)
- **DocRED** (RE, 96 relation types)
- **MAVEN** (Event Detection, 168 event types)

## Reproducing Experiments

### 1. Count Curves (Figure 1a)

Measures how schema size (number of types per prompt) affects extraction performance:

```bash
python scripts/run_d051_count_curves_25.py --dataset fewnerd --seed 42
python scripts/run_d051_count_curves_25.py --dataset fewrel --seed 42
```

Generate the figure:
```bash
python scripts/plot_fig1a_count_curves.py
```

### 2. BCS-Controlled Experiments

Batch Confusability Score (BCS) measures semantic similarity among types in a batch.
This experiment isolates BCS from count by comparing high-BCS vs low-BCS batches at fixed sizes:

```bash
python src/run_batch_composition.py --dataset fewnerd --count 16 --n_batches 25 --seed 42
python src/run_confusability_batch_composition.py --dataset fewrel --count 16 --n_batches 25 --seed 42
```

### 3. Schema Decomposition (SDGD)

Schema-DAG Guided Decomposition splits a large schema into low-confusability sub-batches:

```bash
# Zero-shot SDGD (embedding-based, no calibration needed)
python src/run_sdgd_experiment.py \
    --mode sdgd_zero \
    --dataset fewnerd \
    --types_file configs/few_nerd_types.json \
    --embeddings_path data/embeddings/fewnerd_e5_large.pt \
    --model_path /path/to/Qwen3-32B \
    --output_dir results/sdgd_zero_fewnerd \
    --k 1.0

# Calibrated SDGD (uses confusion matrix from calibration run)
python src/run_sdgd_experiment.py \
    --mode sdgd_cal \
    --dataset fewnerd \
    --types_file configs/few_nerd_types.json \
    --confusion_matrix_path data/calibration/fewnerd_confusion.pt \
    --model_path /path/to/Qwen3-32B \
    --output_dir results/sdgd_cal_fewnerd

# Baselines
python src/run_sdgd_experiment.py --mode single_pass ...   # All types in one batch
python src/run_sdgd_experiment.py --mode per_type ...      # One type per batch (upper bound)
python src/run_sdgd_experiment.py --mode random_batch ...  # Random grouping (ablation)
```

### 4. Cross-Embedding Sensitivity

Tests robustness of BCS across different embedding models:

```bash
python scripts/cross_embedding_sensitivity.py
```

### 5. Relation Extraction (FewRel/DocRED)

```bash
python scripts/run_v2_re_n25.py --dataset fewrel --seed 42
python src/run_docred.py --seed 42
```

### 6. Statistical Analyses (§4.3–4.4)

```bash
# Semipartial R² for BCS after controlling for degree centrality
python scripts/statistical_analyses/compute_semipartial_r2.py \
    --input results/fewrel_batches.json --output results/semipartial_r2.json

# TOST equivalence test for Count × BCS interaction
python scripts/statistical_analyses/factorial_tost.py \
    --input results/fewrel_batches.json --output results/tost.json --delta 3.0

# Permutation-based equivalence test (nonparametric complement)
python scripts/statistical_analyses/permutation_equivalence_test.py \
    --input results/fewrel_batches.json --output results/perm_equiv.json --delta 3.0

# Range-matched interaction analysis (DocRED)
python scripts/statistical_analyses/bcs_range_matched_interaction.py \
    --input results/docred_batches.json --output results/range_matched.json
```

### 7. Figure Generation

```bash
python scripts/gen_fig_count_curves.py        # Figure 1a: count degradation curves
python scripts/gen_fig_bcs_scaling.py          # Figure 1b: BCS-controlled accuracy
python scripts/gen_fig_framework.py            # Figure 2: experimental design overview
python scripts/gen_fig_sdgd_pipeline.py        # Figure 3: SDGD pipeline diagram
```

## Project Structure

```
src/
  few_nerd_utils.py          # Few-NERD data loading
  fewrel_utils.py            # FewRel data loading
  maven_utils.py             # MAVEN data loading
  compute_bcs.py             # Batch Confusability Score computation
  compute_type_embeddings.py # Type embedding generation
  select_type_batches.py     # Schema batch construction
  run_extraction.py          # vLLM-based extraction pipeline
  evaluate.py                # F1/precision/recall evaluation
  bootstrap_ci.py            # Bootstrap confidence intervals
  run_sdgd_experiment.py     # SDGD experiment runner
  run_batch_composition.py   # BCS-controlled experiments
  sdgd/                      # SDGD algorithm module
    similarity.py            # Embedding similarity computation
    graph.py                 # Threshold graph + graph coloring
    decompose.py             # Schema decomposition logic
    merge.py                 # Multi-batch result merging
    evaluate.py              # Decomposition evaluation
    calibrate.py             # Confusion-based calibration

scripts/
  run_d051_count_curves_25.py      # Count curve experiments
  plot_fig1a_count_curves.py       # Figure generation
  gen_fig_count_curves.py          # Figure 1a generation
  gen_fig_bcs_scaling.py           # Figure 1b generation
  gen_fig_framework.py             # Figure 2 generation
  gen_fig_sdgd_pipeline.py         # Figure 3 generation
  compute_e5_embeddings.py         # E5-large embeddings
  cross_embedding_sensitivity.py   # Embedding ablation
  scs_name_def_ablation.py         # Name vs definition ablation
  statistical_analyses/            # §4.3-4.4 statistical tests
    compute_semipartial_r2.py      # Semipartial R² decomposition
    factorial_tost.py              # TOST equivalence test
    permutation_equivalence_test.py # Permutation equivalence
    bcs_range_matched_interaction.py # Range-matched interaction
```

## Citation

```
@article{anonymous2025schema,
  title={Schema-Induced Degradation in Training-Free LLM Information Extraction},
  author={Anonymous},
  year={2025}
}
```
