# IRT Person-Fit Statistics for LLM Benchmark Contamination Detection

Code for the paper: "IRT Person-Fit Statistics for LLM Benchmark Contamination Detection" (EMNLP 2026 submission).

## Overview

This repository implements IRT-based person-fit analysis (lz* statistic) for detecting benchmark contamination in Large Language Models. The method uses 4PL Item Response Theory parameters from the PSN-IRT item bank to compute the Snijders (2001) corrected lz* statistic on binary response patterns. It requires only binary response patterns — no access to model weights, gradients, or training data.

## Repository Structure

```
├── src/                    # Core IRT / person-fit module
│   └── person_fit.py       # 4PL IRT model, lz, lz*, theta MLE, outfit/infit
├── qwen/                   # Qwen-2.5-7B-Instruct experiments
│   ├── prepare_data.py     # Generate training data (clean + contaminated conditions)
│   ├── train.py            # QLoRA SFT training
│   ├── eval_lz.py          # MMLU evaluation + lz* computation
│   └── ...                 # Analysis scripts (Cohen's d, theta-fixed, etc.)
├── llama/                  # Llama-3.1-8B-Instruct experiments
├── mistral/                # Mistral-7B-Instruct-v0.3 experiments
├── scripts/                # Figure generation and simulation scripts
│   ├── gen_appendix_4pl_ablation.py  # 3PL vs 4PL power analysis
│   ├── gen_fig_heatmap.py            # Cohen's d heatmap (Fig. 2)
│   └── gen_fig_theta_scatter.py      # Theta scatter plot (Fig. 3)
├── figures/                # Paper figure generation
│   └── gen_fig1.py         # Response pattern visualization (Fig. 1)
└── requirements.txt
```

## Requirements

- Python 3.10+
- PyTorch 2.x with CUDA support
- See `requirements.txt` for full dependencies

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### 1. Data Preparation

Generate training data with controlled contamination levels:

```bash
cd qwen
python prepare_data.py
```

This creates training sets for conditions: `clean`, `contam_5`, `contam_15`, `contam_25`, `contam_50` (varying percentages of MMLU items mixed into Alpaca SFT data).

### 2. Training (QLoRA SFT)

```bash
python train.py --condition contam_15 --gpu 0
```

**Conditions:** `clean_s1`, `clean_s2`, ..., `contam_5`, `contam_15`, `contam_25`, `contam_50`

### 3. Evaluation (lz* computation)

```bash
python eval_lz.py --condition contam_15 --gpu 0
```

Evaluates the fine-tuned adapter on full MMLU using 3-shot prompting and computes:
- Theta MLE (ability estimate)
- lz* (Snijders 2001 corrected person-fit statistic)
- Accuracy (overall, seen items, unseen items)

### 4. Statistical Analysis

```bash
python compute_delta.py          # Delta lz* and summary statistics
python unified_lz_recompute.py   # Unified recomputation with theta-fixed analysis
python compute_cohens_d.py       # Cohen's d with bootstrap CIs
```

### 5. Cross-Model Replication

The `llama/` and `mistral/` directories contain analogous scripts for Llama-3.1-8B-Instruct and Mistral-7B-Instruct-v0.3. Usage is identical.

## Configuration

Before running, update the `BASE_DIR` and model path constants in each script to point to your local directories. Models used:
- `Qwen/Qwen2.5-7B-Instruct`
- `meta-llama/Llama-3.1-8B-Instruct`
- `mistralai/Mistral-7B-Instruct-v0.3`

## Data

- MMLU items from `cais/mmlu` (HuggingFace datasets)
- 4PL IRT parameters from PSN-IRT item bank (place `mmlu_params.csv` in each model directory)
- Alpaca SFT data from `tatsu-lab/alpaca`

## License

[To be added after review]
