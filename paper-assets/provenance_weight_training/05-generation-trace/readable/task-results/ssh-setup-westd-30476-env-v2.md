# ssh setup westd 30476 env v2

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_setup_westd_30476_env_v2_20260517T101635_result.json`
- **Structured JSON:** [`ff5595978472e6b677f2.json`](../../sessions/ff/ff5595978472e6b677f2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Server Status Summary: westd-30476

| Item | Status | Details |
|------|--------|---------|
| **SSH** | OK | Connected successfully |
| **OS/Kernel** | Ubuntu, 5.15.0-78-generic x86_64 | Up 218 days |
| **GPUs** | 4x NVIDIA RTX PRO 6000 Blackwell | ~96 GB VRAM each, Driver 580.82, CUDA 13.0 |
| **Disk (root `/`)** | 30G total, 4% used (29G free) | |
| **Disk (`/dev/sda2`)** | 879G total, 3% used (816G free) | |
| **Disk (shared NFS)** | 7.3T total, 24% used (5.3T free) | `/autodl-pub` |
| **Python** | **MISSING** | No python3 found anywhere |
| **Conda** | **MISSING** | No conda/miniconda |
| **PyTorch** | **MISSING** | No pip packages installed |
| **Pre-built image** | **No** | No `.aml_image.json` detected |
| **Project code dir** | Exists (`/root/provenance_weight_training/`) | Contains `data/` and `models/` subdirs, but **empty** (no files) |
| **Training data** | **MISSING** | No `scored_data.jsonl` or `eval_holdout.jsonl` found |
| **Model weights** | **MISSING** | No `Qwen3-0.6B` directory found |

### What needs to be done

1. **Install Python 3.10+** (miniconda or system package)
2. **Install PyTorch** (compatible with CUDA 13.0 / Blackwell GPUs)
3. **Install ML packages**: transformers, accelerate, peft, trl, datasets, wandb, etc.
4. **Transfer project code** to `/root/provenance_weight_training/`
5. **Transfer training data**: `scored_data.jsonl`, `eval_holdout.jsonl`
6. **Download or transfer model weights**: Qwen3-0.6B

The server is a bare container with only GPU drivers installed. Full environment setup is required.

---
