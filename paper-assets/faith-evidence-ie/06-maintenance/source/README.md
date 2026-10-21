# FREIGE: Faithful Relation Extraction with Evidence-Grounded Generation

Code for the paper: *Evidence-Grounded Document-Level Relation Extraction via Contrastive Evidence Discrimination*.

## Overview

FREIGE is a framework for document-level relation extraction (DocRE) that jointly extracts relation triples and their supporting evidence sentences. The key components are:

1. **SFT (Supervised Fine-Tuning)**: Fine-tune an LLM with QLoRA on DocRED data to output structured relation triples with evidence.
2. **RSFT (Rejection Sampling Fine-Tuning)**: Improve the SFT model through iterative self-refinement:
   - Generate multiple candidate outputs via temperature sampling
   - Score candidates using the CED (Contrastive Evidence Discrimination) reward
   - Fine-tune on top-scoring candidates
3. **CED Reward**: An NLI-based reward that measures evidence faithfulness by contrasting cited evidence against hard negatives.

## Installation

```bash
pip install -r requirements.txt
```

## Data Preparation

Download [DocRED](https://github.com/thunlp/DocRED) or [Re-DocRED](https://github.com/tonytan48/Re-DocRED) and place files under `./data/docred/`:

```
data/docred/
├── train_annotated.json
├── dev.json
├── test.json
└── rel_info.json
```

For Re-DocRED, use the conversion script:
```bash
python scripts/convert_redocred.py --input_dir /path/to/re-docred --output_dir ./data/docred
```

## Pipeline

### Step 1: SFT Training

```bash
# Single GPU (4-bit QLoRA)
python -m freige.training.sft_trainer \
    --model_name /path/to/base-model \
    --data_dir ./data/docred \
    --output_dir ./outputs/sft \
    --lora_rank 64 --lora_alpha 128 \
    --per_device_batch_size 2 --num_epochs 3 \
    --seed 42

# Multi-GPU with DeepSpeed
accelerate launch --config_file configs/accelerate_4gpu.yaml \
    -m freige.training.sft_trainer \
    --deepspeed configs/deepspeed_zero2.json \
    --model_name /path/to/base-model \
    --data_dir ./data/docred \
    --output_dir ./outputs/sft \
    --no_quantize --bf16
```

### Step 2: RSFT Candidate Generation

```bash
python -m freige.training.rsft_generate \
    --base_model /path/to/base-model \
    --sft_adapter ./outputs/sft \
    --data_path ./data/docred \
    --output_dir ./outputs/rsft_candidates \
    --num_generations 8 --temperature 0.7
```

### Step 3: CED Scoring & Filtering

```bash
python -m freige.training.rsft_score_filter \
    --generations_path ./outputs/rsft_candidates/generations.jsonl \
    --data_path ./data/docred \
    --output_dir ./outputs/rsft_scored \
    --top_k 1
```

### Step 4: RSFT Training

```bash
python -m freige.training.rsft_trainer \
    --base_model /path/to/base-model \
    --sft_adapter ./outputs/sft \
    --rsft_data_path ./outputs/rsft_scored/rsft_train.jsonl \
    --output_dir ./outputs/rsft
```

### Step 5: Evaluation

```bash
python -m freige.eval.inference \
    --model_path ./outputs/rsft \
    --base_model /path/to/base-model \
    --data_path ./data/docred \
    --split dev \
    --output_dir ./outputs/eval_results
```

Metrics reported: F1, Ign-F1, Evi-F1, and EDCR (Evidence-Discriminated Completeness Ratio).

## Project Structure

```
freige/
├── data/           # Data loading and preprocessing (DocRED processor)
├── eval/           # Inference, evaluation metrics, CED-based reranking
├── rewards/        # CED reward model
├── training/       # SFT, RSFT, GRPO trainers and utilities
configs/            # DeepSpeed and Accelerate configurations
scripts/            # Training, evaluation, and utility shell scripts
tests/              # Unit tests
```

## Test Set Submission

For Re-DocRED test set evaluation, generate CodaLab-format predictions:
```bash
python -m freige.eval.inference \
    --model_path ./outputs/rsft \
    --base_model /path/to/base-model \
    --data_path ./data/docred \
    --split test \
    --output_dir ./outputs/test_submission
```
The output `codalab_submission.json` can be submitted to the [CodaLab leaderboard](https://codalab.lisn.upsaclay.fr/competitions/365).
