# SF8: Reproducibility Details

## LoRA Configuration

All four fine-tuned models (Qwen3-8B and Llama-3.1-8B-Instruct, on SciERC and DocRED) share the same LoRA hyperparameters.

| Parameter | Value |
|-----------|-------|
| Rank (r) | 16 |
| Alpha | 32 |
| Dropout | 0.05 |
| Bias | none |
| Target modules | q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj |
| Task type | CAUSAL_LM |

## Training Configuration

| Parameter | SciERC | DocRED |
|-----------|--------|--------|
| Base models | Qwen3-8B / Llama-3.1-8B-Instruct | Qwen3-8B / Llama-3.1-8B-Instruct |
| Train examples | 1,762 | 3,053 |
| Dev examples | 260 | 998 |
| Epochs | 3 | 3 |
| Per-device batch size | 4 | 2 |
| Gradient accumulation steps | 4 | 8 |
| Effective batch size | 16 | 16 |
| Max sequence length | 2,048 | 4,096 |
| Learning rate | 2e-4 | 2e-4 |
| LR scheduler | Cosine | Cosine |
| Warmup ratio | 0.1 | 0.1 |
| Warmup steps | 33 | 57 |
| Total training steps | 333 | 573 |
| Optimizer | AdamW (torch) | AdamW (torch) |
| Precision | bf16 | bf16 |
| Gradient checkpointing | Yes | Yes |
| Loss | Completion-only | Completion-only |
| Seed | 42 | 42 |

## Hardware

- GPU: 2x NVIDIA RTX PRO 6000 Blackwell Server Edition (98 GB VRAM each); single GPU used per training run
- Estimated training time (SciERC): ~11 min per model
- Estimated training time (DocRED): ~1.5 h per model

## Software

| Package | Version |
|---------|---------|
| PyTorch | 2.10 |
| Transformers | 4.57 |
| PEFT | 0.19 |
| TRL | 1.1 |
| Accelerate | 1.13 |

## Inference Time (seconds/document)

### Qwen3-8B (zero-shot, greedy decoding)

| Configuration | SciERC (mean +/- std) | DocRED (mean +/- std) |
|--------------|----------------------|----------------------|
| Unconstrained | 8.69 +/- 3.89 | 19.75 +/- 8.99 |
| Grammar-only | 8.81 +/- 4.51 | 20.58 +/- 10.75 |
| Semantic-only | 7.23 +/- 3.91 | 20.53 +/- 9.37 |
| Full S1 | 6.76 +/- 3.67 | 20.39 +/- 9.43 |
| Post-hoc | 8.69 +/- 3.89 | 19.78 +/- 8.99 |

### Llama-3.1-8B-Instruct (zero-shot, greedy decoding)

| Configuration | SciERC (mean +/- std) | DocRED (mean +/- std) |
|--------------|----------------------|----------------------|
| Unconstrained | 2.81 +/- 1.65 | 18.16 +/- 12.88 |
| Full S1 | 4.33 +/- 3.15 | 20.52 +/- 15.62 |

### Beam Search (k=4, Full S1)

| Model | SciERC (mean +/- std, n=551) | DocRED (mean +/- std, n=50) |
|-------|------------------------------|----------------------------|
| Qwen3-8B | 5.92 +/- 2.34 | 31.35 +/- 26.09 |
| Llama-3.1-8B | 4.81 +/- 2.33 | 20.78 +/- 10.08 |

### Constrained Decoding Overhead (Qwen3-8B, vs. Unconstrained)

| Configuration | SciERC overhead | DocRED overhead |
|--------------|----------------|----------------|
| Grammar-only | +1.4% | +4.2% |
| Semantic-only | -16.9% | +3.9% |
| Full S1 | -22.2% | +3.2% |
| Post-hoc | ~0% | +0.1% |

Note: Negative overhead on SciERC indicates that constrained decoding reduced generation length (and thus inference time) by suppressing invalid tokens early. On DocRED (longer documents), the masking computation adds a small constant overhead that slightly exceeds any token-savings effect.

## Runtime Summary

| Dataset | Model | Config | Total time (min) | Docs |
|---------|-------|--------|-----------------|------|
| SciERC | Qwen3-8B | Unconstrained | 79.8 | 551 |
| SciERC | Qwen3-8B | Full S1 | 62.1 | 551 |
| SciERC | Llama-3.1-8B | Unconstrained | 25.8 | 551 |
| SciERC | Llama-3.1-8B | Full S1 | 39.7 | 550 |
| DocRED | Qwen3-8B | Unconstrained | 328.6 | 998 |
| DocRED | Qwen3-8B | Full S1 | 339.2 | 998 |
| DocRED | Llama-3.1-8B | Unconstrained | 302.1 | 998 |
| DocRED | Llama-3.1-8B | Full S1 | 341.4 | 998 |
