# ThreadGate: Turn-Aware Residual Gating for Multi-Turn LLMs

Code for the paper *"From Collapse to Recovery: Diagnosing and Mitigating Exposure Bias in Multi-Turn Attention Objectives"*.

## Overview

ThreadGate adds lightweight, turn-aware gates to each transformer layer's residual connection. The gate modulates how much of the layer's computation is applied based on turn-level positional features (distance from turn boundary, absolute turn index), preserving goal-directed attention (GAR) across long conversations without degrading fluency.

**Key components:**
- `threadgate.py` — ThreadGatedModel with per-layer gate networks and TurnEmbedding
- `gar.py` — Goal Attention Ratio (GAR) measurement and auxiliary loss
- `turn_utils.py` — Turn boundary detection for ChatML and Llama-3 templates
- `attention_steering.py` — Inference-time pre-softmax attention bias
- `split_softmax.py` — Li et al. (2024) post-softmax rescaling baseline

## Requirements

- Python 3.10+
- CUDA-capable GPU with >= 24GB VRAM (e.g., A6000, A100)

```bash
pip install -r requirements.txt
```

## Data Preparation

```bash
python data/download_ultrachat.py --output-dir data/ultrachat_8k --num-samples 8000
```

This downloads UltraChat-200K from HuggingFace, filters for conversations with >= 5 assistant turns, and samples 8K examples.

To create the held-out evaluation split:

```bash
python data/convert_to_eval.py --data-dir data/ultrachat_8k --output data/ultrachat_eval_heldout.json --num-samples 50
```

## Training

All training scripts accept an optional seed argument (default: 42). Training runs on a single GPU.

### ThreadGate (full method)

```bash
bash scripts/train_threadgate.sh 42
```

### Baselines and Ablations

```bash
# LoRA-only (no gating)
bash scripts/train_lora_only.sh 42

# Uniform Gate (gate without turn-awareness)
bash scripts/train_uniform_gate.sh 42

# PCGrad (gradient conflict resolution, Yu et al. NeurIPS 2020)
bash scripts/train_pcgrad.sh 42

# Scheduled Sampling (exposure bias mitigation)
bash scripts/train_scheduled_sampling.sh 42
```

### Multi-seed Runs

```bash
for seed in 42 123 456; do
  bash scripts/train_threadgate.sh $seed
  bash scripts/train_lora_only.sh $seed
  bash scripts/train_uniform_gate.sh $seed
  bash scripts/train_pcgrad.sh $seed
  bash scripts/train_scheduled_sampling.sh $seed
done
```

### Cross-model (Llama-3.1-8B-Instruct)

```bash
python src/train.py \
  --model meta-llama/Llama-3.1-8B-Instruct \
  --gate-type threadgate \
  --gar-loss-mode mse_target --gar-target 0.5 \
  --lambda-gar 1.0 --lambda-gate-div 1.0 \
  --min-gate-std 0.05 --init-bias 1.5 \
  --gate-lr-multiplier 10 \
  --seed 42 --epochs 3 \
  --output-dir runs/llama_threadgate_s42 \
  --data-dir data/ultrachat_8k
```

## Evaluation

### GAR (Goal Attention Ratio)

```bash
# Teacher-forced GAR evaluation
bash scripts/eval_gar.sh runs/threadgate_s42 threadgate

# Base model baseline
python src/eval_gar.py --gate-type baseline --output-dir results/
```

### Attention Steering

```bash
bash scripts/eval_attention_steering.sh runs/threadgate_s42 threadgate
```

### Gradient Conflict Analysis

```bash
python src/gradient_conflict_analysis.py \
  --checkpoint-dir runs/threadgate_s42 \
  --data-dir data/ultrachat_8k \
  --output results/gradient_conflict.json
```

## Hyperparameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| LoRA rank | 16 | Applied to q_proj, v_proj |
| LoRA alpha | 32 | |
| Gate hidden dim | 64 | |
| Turn embed dim | 16 | 8 for distance + 8 for index |
| Max turn distance | 32 | Bucket cap for distance embedding |
| Learning rate | 2e-4 | Base LR for LoRA params |
| Gate LR multiplier | 10x | Gates train at 2e-3 |
| GAR loss mode | mse_target | Bidirectional MSE toward target |
| GAR target | 0.5 | Target GAR ratio |
| Lambda GAR | 1.0 | GAR loss weight |
| Lambda gate div | 1.0 | Gate diversity regularizer weight |
| Min gate std | 0.05 | Minimum cross-layer gate std |
| Init bias | 1.5 | Gate initialized near-open |
| Batch size | 1 | Per-GPU |
| Grad accumulation | 8 | Effective batch size = 8 |
| Max seq length | 2048 | |
| Epochs | 3 | |

## Repository Structure

```
src/
  config.py                      # Hyperparameter defaults (Qwen)
  config_llama.py                # Llama-3.1 config override
  threadgate.py                  # ThreadGatedModel, TurnEmbedding, GateNetwork
  gar.py                         # GAR measurement + auxiliary loss
  turn_utils.py                  # Turn boundary detection (ChatML / Llama-3)
  model_loader.py                # Checkpoint loading for inference
  attention_steering.py          # Pre-softmax attention bias
  split_softmax.py               # Li et al. (2024) baseline
  trc_measure.py                 # Turn Representation Coherence metric
  train.py                       # Base training (ThreadGate / UG / LoRA-only)
  train_pcgrad.py                # PCGrad training variant
  train_scheduled_sampling.py    # Scheduled Sampling training variant
  eval_gar.py                    # GAR evaluation
  eval_multiturn.py              # Multi-turn instruction following evaluation
  eval_attention_steering.py     # Attention steering evaluation
  gradient_conflict_analysis.py  # NTP vs GAR gradient analysis
data/
  download_ultrachat.py          # Download + prepare UltraChat-8K
  convert_to_eval.py             # Create held-out eval split
scripts/
  train_threadgate.sh            # ThreadGate training
  train_uniform_gate.sh          # Uniform Gate ablation
  train_lora_only.sh             # LoRA-only baseline
  train_pcgrad.sh                # PCGrad training
  train_scheduled_sampling.sh    # Scheduled Sampling training
  eval_gar.sh                    # GAR evaluation
  eval_attention_steering.sh     # Attention steering evaluation
  eval_multiturn.sh              # Multi-turn instruction following evaluation
requirements.txt
```

## License

MIT
