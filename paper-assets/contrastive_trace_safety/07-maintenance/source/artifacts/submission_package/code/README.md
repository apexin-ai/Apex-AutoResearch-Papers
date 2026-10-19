# Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models

Anonymous submission to ARR May 2026.

## Directory Structure

```
code/
├── src/                          # Core library
│   ├── config.py                 # Central configuration (paths, hyperparameters)
│   ├── data_loader.py            # HarmThoughts dataset loading & CP extraction
│   ├── extract_hidden_states.py  # Hidden state extraction from transformer layers
│   ├── run_pipeline.py           # Main pipeline entry point (extract/train/eval)
│   ├── advbench/                 # AdvBench cross-dataset modules
│   │   ├── extract_hidden_states.py
│   │   └── extract_text_embeddings.py
│   ├── baselines/
│   │   └── linear_probe.py       # Static linear probe & MLP baseline
│   ├── crta/
│   │   └── temporal_probe.py     # Temporal window probe (sliding window MLP)
│   ├── eval/
│   │   └── evaluate.py           # Step-level accuracy, detection lead time, FPR
│   └── experiments/
│       ├── bootstrap_ci.py       # Bootstrap CI & paired significance tests
│       ├── exp_r3_ccs_probe.py   # CCS unsupervised probe baseline
│       ├── fpr_analysis.py       # False positive rate analysis
│       └── trajguard_mahalanobis.py  # Mahalanobis distance baseline
├── scripts/                      # Experiment runner scripts
│   ├── advbench_preliminary_sweep.py      # Layer sweep (25L × 4W × 5 metrics)
│   ├── advbench_preliminary_sweep_no_pca.py  # Layer sweep without PCA
│   ├── advbench_hs_exploratory.py         # AdvBench exploratory analysis
│   ├── heuristic_cp.py                    # Heuristic commitment point detection
│   ├── n6_multi_metric_ensemble.py        # Three-layer ensemble (Table 4)
│   ├── random_cp_control_qwq32b.py        # Random-label control experiment
│   ├── run_7b8b_residualization.py        # Position residualization (7-8B)
│   ├── run_a7_random_projection.py        # Random projection baseline
│   ├── run_threshold_sensitivity.py       # K-threshold sensitivity ablation
│   └── sf3_quadratic_residual.py          # Quadratic residualization analysis
├── reproduce/                    # One-click reproduction scripts
│   ├── reproduce_table2.sh       # HS vs. text comparison (Table 2)
│   ├── reproduce_table3.sh       # Layer selection sensitivity (Table 3)
│   └── reproduce_table4.sh       # Ensemble results (Table 4)
└── requirements.txt
```

## Setup

### 1. Environment

```bash
conda create -n cts python=3.10 -y
conda activate cts
pip install -r requirements.txt
```

GPU requirement: 1× 24GB GPU (RTX 4090 / A5000) for 7-8B models; 2× 24GB or 1× 48GB for 32B models.

### 2. Data Preparation

**HarmThoughts dataset** (auto-downloaded from HuggingFace Hub):
```bash
# The dataset loads automatically via the `datasets` library.
# No manual download needed. Requires internet access on first run.
```

**AdvBench** (for cross-dataset analysis only):
The AdvBench prompts are loaded programmatically. See `scripts/heuristic_cp.py` for details.

### 3. Environment Variables

```bash
export DATA_DIR=/path/to/project/root    # Where artifacts/ will be created
export MODEL_DIR=/path/to/model/weights  # HuggingFace model cache
```

### 4. Hidden State Extraction

Before running experiments, extract hidden states for each model:

```bash
# R1-8B (primary model, layers 12-24)
python -m src.run_pipeline --step extract

# For full 25-layer sweep (AdvBench analysis)
python -m src.advbench.extract_hidden_states --output-dir $DATA_DIR/artifacts/hidden_states_all25
```

For 32B models, adjust `src/config.py` to point to the appropriate model and layer range.

## Reproducing Main Results

### Table 2: HS vs. Text Comparison
```bash
bash reproduce/reproduce_table2.sh
```
Runs bootstrap CI (10,000 resamples) comparing HS and text probe precision at threshold-based layers across 4 models. Expected output: HS precision advantage of +15.4 to +21.9pp (384d encoder).

### Table 3: Layer Selection Sensitivity
```bash
bash reproduce/reproduce_table3.sh
```
Demonstrates that crossing-rate composite metrics select shallow layers (L0-L10) while threshold-based metrics select deep layers (L14-L63). Includes random-CP control.

### Table 4: Three-Layer Ensemble
```bash
bash reproduce/reproduce_table4.sh
```
Shows metric-agnostic HS advantage via ensemble of precision-best, BA-best, and FPR-best layers (all 4 models, p <= 0.002).

## Models Evaluated

| Model | Architecture | Params | Layers | Hidden Dim |
|-------|-------------|--------|--------|------------|
| R1-8B | Llama-8B (R1-distilled) | 8B | 32 | 4096 |
| OT-7B | Qwen-7B (OpenThinker) | 7B | 28 | 3584 |
| QwQ-32B | Qwen-32B (native reasoning) | 32B | 64 | 5120 |
| R1-32B | Qwen-32B (R1-distilled) | 32B | 64 | 5120 |

## Key Hyperparameters

- Probe: L2-regularized logistic regression (C=1.0)
- Temporal window: W selected from {1, 3, 5, 10, 15, 20, 25} on validation
- Detection: K=5 consecutive threshold crossings
- Data split: 60/20/20 (train/val/test) at trace level
- Bootstrap: 10,000 resamples with BCa intervals
- Correction: Holm-Bonferroni at alpha=0.05
