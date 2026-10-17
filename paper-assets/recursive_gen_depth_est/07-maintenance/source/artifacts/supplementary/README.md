# Supplementary Material: Recursive Generation Depth Estimation

## Repository Structure

```
├── scripts/                    # Pipeline and evaluation scripts
│   ├── lora_finetune.py        # LoRA fine-tuning (r=16, α=32, 3 epochs)
│   ├── generate_next_depth.py  # BOS-seeded generation for next depth
│   ├── run_pipeline.sh         # End-to-end pipeline (Pythia nucleus)
│   ├── run_pipeline_*.sh       # Per-cell pipeline variants (9 cells)
│   ├── atlas_analysis.py       # Atlas feature importance analysis
│   ├── d4_extension_eval*.py   # Depth extension (d4-d5) evaluation
│   ├── baseline_*.py           # Baseline methods (CORAL, DivEye, CE, ppl regression, zero-shot LLM)
│   ├── detection_baselines.py  # DetectGPT / Min-K% Prob baselines
│   └── prompted_generation_eval.py  # Topic-seeded generation validation
├── src/                        # Core analysis modules
│   ├── atlas_v2.py             # 9-cell atlas construction and RF training
│   ├── cross_model_loo.py      # Leave-one-model-family-out transfer
│   ├── binary_pairwise_eval.py # Pairwise AUC for EDD computation
│   ├── wild_data_calibration.py # Cross-domain FPR (C4, FineWeb, WikiText)
│   ├── w2_domain_bias.py       # LOGO / seed-group domain bias control
│   └── curation_poc.py         # Depth-graduated curation probe
├── docs/paper/                 # LaTeX source
│   ├── main.tex                # Main document
│   ├── section_appendix.tex    # Appendix (B.1-B.21)
│   └── figures/                # PDF figures (4 main + appendix)
└── artifacts/                  # Experiment outputs and analysis
```

## Data Access

**Seed corpus**: Wikipedia subset (English), publicly available.

**Generated data**: 180K samples across 9 model-strategy cells (3 models × 3 strategies × 4 depths × 5,000 samples). Feature files (19-dimensional vectors per passage) will be released upon acceptance.

**Models used**:
- Pythia-1.4B (EleutherAI) — [HuggingFace](https://huggingface.co/EleutherAI/pythia-1.4b)
- OLMo-1B (AI2) — [HuggingFace](https://huggingface.co/allenai/OLMo-1B)
- GPT-2 XL (OpenAI, 1.5B) — [HuggingFace](https://huggingface.co/openai-community/gpt2-xl)
- Qwen2.5-14B (cross-scale) — [HuggingFace](https://huggingface.co/Qwen/Qwen2.5-14B)

No fine-tuned checkpoints are released (LoRA adapters are depth-specific and not reusable).

## Reproduction Steps

### 1. Environment Setup

```bash
pip install torch transformers peft datasets scikit-learn scipy numpy
```

Required: Python >= 3.10, PyTorch >= 2.0, CUDA >= 11.8.

### 2. Full Pipeline (Single Cell)

```bash
# Example: Pythia-1.4B, nucleus sampling
bash scripts/run_pipeline.sh
```

Each pipeline script executes:
1. LoRA fine-tuning on depth-(k-1) data (r=16, α=32, lr=2e-4, batch=16, 3 epochs, dropout=0.05)
2. BOS-seeded generation (5,000 samples, max 512 tokens)
3. Feature extraction (19 features via Pythia-1.4B reference)
4. Repeat for depths d1-d3

### 3. Atlas Construction and Evaluation

```bash
python src/atlas_v2.py          # 9-cell RF training + 5-fold CV
python src/binary_pairwise_eval.py  # EDD pairwise AUC computation
python scripts/atlas_analysis.py    # Feature importance (Gini + SHAP)
```

### 4. Generalization Experiments

```bash
python src/cross_model_loo.py       # Cross-model transfer (Table 4)
python scripts/baseline_coral.py    # CORAL ordinal baseline
python scripts/baseline_diveye_ordinal.py  # DivEye baseline
python scripts/detection_baselines.py      # DetectGPT, Min-K% Prob
```

### 5. Cross-Domain Evaluation

```bash
python src/wild_data_calibration.py  # C4, FineWeb, WikiText FPR
python src/w2_domain_bias.py         # LOGO domain bias control
```

## Key Hyperparameters

| Parameter | Value | Notes |
|-----------|-------|-------|
| LoRA rank (r) | 16 | Fixed across all experiments |
| LoRA alpha (α) | 32 | |
| Learning rate | 2e-4 | |
| Batch size (effective) | 16 | |
| Epochs | 3 | Per depth cycle |
| Dropout | 0.05 | |
| RF trees (main) | 200 | 5-fold stratified CV |
| RF trees (EDD binary) | 500 | Per adjacent pair |
| Generation max tokens | 512 | BOS-seeded |
| Samples per depth | 5,000 | Per cell |
| Random seed | 42 | seed=43 for replication (3/9 cells) |

## Computational Requirements

- **GPU**: NVIDIA RTX 6000 Pro (48GB) or equivalent
- **Per-cell pipeline**: ~8-12 hours (fine-tuning + generation + feature extraction, 4 depths)
- **Full 9-cell benchmark**: ~72-108 GPU-hours
- **Cross-scale (14B)**: ~25 hours per strategy on single GPU
- **Analysis (RF, baselines)**: CPU-only, < 1 hour total

## Anonymization Note

This supplementary material is provided for review purposes. All identifying information has been removed. Code and data release will follow upon acceptance.
