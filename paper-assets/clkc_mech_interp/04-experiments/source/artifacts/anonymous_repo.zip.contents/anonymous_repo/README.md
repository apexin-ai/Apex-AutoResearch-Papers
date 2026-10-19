# Cross-Lingual Knowledge Conflict: A Mechanistic Interpretability Study

Code for the paper: *[Title anonymized for review]*

## Overview

This repository provides the full experimental pipeline for probing **cross-lingual knowledge conflicts** in large language models via mechanistic interpretability. We train linear and MLP probes on residual stream activations to detect conflict signals, analyze cross-lingual transfer asymmetry, and perform causal validation through representation steering.

**Models studied:** Llama-3.1-8B-Instruct (32 layers), Gemma-2-9B-IT (42 layers), Qwen3-8B-Instruct (36 layers)

**Languages:** English (EN), Chinese (ZH), German (DE)

## Repository Structure

```
├── src/
│   ├── collect_activations.py       # Hook transformer layers, save residual stream activations
│   ├── train_probe.py               # Per-layer LogisticRegression probes with multi-seed resplit
│   ├── train_mlp_probe.py           # MLP probe (1-hidden-layer, 256-dim) for nonlinearity comparison
│   ├── steering_experiment.py       # Causal intervention via probe weight steering vectors
│   ├── bootstrap_probe.py           # Fast parallel bootstrap with multiprocessing (COW memory)
│   ├── bootstrap_asymmetry.py       # Bootstrap CI for ZH→EN vs EN→ZH transfer asymmetry
│   ├── bootstrap_mlp_delta.py       # Bootstrap MLP vs Linear probe delta
│   ├── compute_auroc.py             # AUROC across models and cross-lingual directions
│   ├── compute_cka.py               # Layer-wise Linear CKA and SVCCA (aligned + shuffled)
│   ├── cross_task_transfer.py       # Train probes on conflict, evaluate on XNLI (and vice versa)
│   ├── cross_task_transfer_bootstrap.py  # Bootstrap CI for cross-task transfer
│   ├── probe_cosine_similarity.py   # Cosine similarity between conflict and XNLI probe weights
│   ├── comet_tertile_ablation.py    # COMET score tertile ablation + Fisher exact test
│   ├── tost_equivalence.py          # TOST equivalence test: conflict vs XNLI asymmetry
│   ├── tost_power_analysis.py       # TOST power analysis + Bayesian BF01
│   ├── random_labels_control.py     # Permuted-label probes for selectivity baseline
│   ├── token_overlap_analysis.py    # Per-sample token overlap, correlation, tercile control
│   ├── verify_parametric_knowledge.py  # Verify model's own parametric knowledge, relabel conflicts
│   ├── translate.py                 # EN→ZH / EN→DE translation via LLM
│   ├── validate_translation.py      # Back-translation + COMET quality validation
│   ├── prepare_xnli.py             # Prepare XNLI as non-conflict semantic baseline
│   └── supplement_sampling.py       # Supplement sampling from ConflictQA
├── scripts/
│   ├── run_pipeline.sh              # End-to-end reproduction script
│   └── run_probes.sh                # XNLI baseline probe training
├── requirements.txt
├── LICENSE
└── README.md
```

## Environment Setup

```bash
# Python >= 3.10, CUDA >= 12.1 recommended
pip install -r requirements.txt

# For flash-attention (optional, speeds up activation collection):
pip install flash-attn --no-build-isolation
```

## Data Acquisition

1. **ConflictQA** (Xie & Min, 2024): Download from [HuggingFace](https://huggingface.co/datasets/liangyuxin/ConflictQA) — use the `popQA-chatgpt` subset.

2. **XNLI** (Conneau et al., 2018): Auto-downloaded by `prepare_xnli.py`.

3. **Models**: Download from HuggingFace:
   - `meta-llama/Llama-3.1-8B-Instruct`
   - `google/gemma-2-9b-it`
   - `Qwen/Qwen3-8B-Instruct`

## Reproduction

### Full pipeline (single model)

```bash
bash scripts/run_pipeline.sh meta-llama/Llama-3.1-8B-Instruct llama31 32
```

### Step-by-step

```bash
# 1. Prepare data
python src/supplement_sampling.py --dataset_path data/conflictQA-popQA-chatgpt.json --data_dir data/
python src/verify_parametric_knowledge.py --model <MODEL> --data_dir data/ --raw_dir data/ --output_dir data/
python src/translate.py --model <MODEL> --target_lang zh --input_dir data/ --output_dir data/
python src/validate_translation.py --model <MODEL> --source_lang_dir data/ --en_dir data/ --output_dir data/

# 2. Collect activations
python src/collect_activations.py --model <MODEL> --data_dir data/ --output_dir data/<key>/ --lang en
python src/collect_activations.py --model <MODEL> --data_dir data/ --output_dir data/<key>/ --lang zh

# 3. Train probes
python src/train_probe.py --activation_dir data/<key>/ --output_dir data/<key>/ --seeds 42,123,456,789,1024

# 4. Analysis
python src/bootstrap_probe.py --activation_dir data/<key>/ --output_dir results/<key>/
python src/steering_experiment.py --model <MODEL> --data_dir data/<key>/ --output_dir results/<key>/
python src/compute_cka.py --models '<JSON config>' --output results/cka_results.json
```

### XNLI baseline

```bash
python src/prepare_xnli.py --output_dir data/xnli/
python src/collect_activations.py --model <MODEL> --data_dir data/xnli/ --output_dir data/xnli/<key>/ --lang en
bash scripts/run_probes.sh <key>
```

## Key Experiments

| Script | Purpose |
|--------|---------|
| `train_probe.py` | Core finding: linear probes detect conflict in residual stream |
| `steering_experiment.py` | Causal validation via activation steering |
| `bootstrap_probe.py` | Statistical robustness with 2000-iteration bootstrap |
| `cross_task_transfer.py` | Whether conflict and XNLI share cross-lingual subspace |
| `comet_tertile_ablation.py` | Control: translation quality not a confounder |
| `random_labels_control.py` | Control: probes are selective, not fitting noise |
| `token_overlap_analysis.py` | Control: token overlap does not drive probe accuracy |

## Citation

```bibtex
@inproceedings{anonymous2026clkc,
  title     = {[Title anonymized for review]},
  author    = {Anonymous},
  booktitle = {Proceedings of EMNLP 2026},
  year      = {2026},
}
```
