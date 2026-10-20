# GPU Environment Report — agent_progress_probe

**Server:** autodl-5090 (gpu-5090-2x-2)
**Date:** 2026-05-14

## System

| Item | Value |
|------|-------|
| Python | 3.12.3 (miniconda3) |
| PyTorch | 2.10.0+cu128 |
| CUDA | 12.8 (driver 580.105.08) |
| Transformers | 4.57.6 |
| Accelerate | 1.13.0 |
| W&B | 0.26.0 |

## GPU

| GPU | Model | VRAM |
|-----|-------|------|
| cuda:0 | NVIDIA GeForce RTX 5090 | 31 GB |
| cuda:1 | NVIDIA GeForce RTX 5090 | 31 GB |

## Disk

| Mount | Total | Used | Available |
|-------|-------|------|-----------|
| /root/autodl-tmp | 250 GB | 1.5 GB | 249 GB |

HF cache: `/root/autodl-tmp/.hf_cache/` (1.2 GB)

## Qwen3-Embedding-0.6B Test

| Metric | Value |
|--------|-------|
| Embedding shape | [1, 1024] |
| GPU memory used | 2.23 GB |
| Status | OK |

## Conda Activation

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
```

## Pre-installed ML Packages

- torch 2.10.0+cu128
- transformers 4.57.6
- accelerate 1.13.0
- einops 0.8.2
- sentencepiece 0.2.1
- sentence-transformers 5.4.1
- wandb 0.26.0
- tqdm 4.67.3
- flashinfer-python 0.6.6
