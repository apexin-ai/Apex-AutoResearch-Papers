# setup env westd 29046

**tbab multi turn** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_setup_env-westd-29046_20260518T061704_result.json`
- **Structured JSON:** [`2c74fc2e7d8390cb1cbc.json`](../../sessions/2c/2c74fc2e7d8390cb1cbc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All done. Final report:

---

## Environment Setup Report — westd-29046

### Python / CUDA / PyTorch
| Item | Value |
|------|-------|
| Python | 3.10.12 |
| PyTorch | 2.12.0+cu130 |
| CUDA available | True |
| CUDA driver | 595.58.03 |
| bf16 supported | True |

### GPU
| GPU | Name | VRAM |
|-----|------|------|
| 0 | NVIDIA RTX PRO 6000 Blackwell Server Edition | 94 GB |
| 1 | NVIDIA RTX PRO 6000 Blackwell Server Edition | 94 GB |

### Package Versions
| Package | Version |
|---------|---------|
| transformers | 5.8.1 |
| peft | 0.19.1 |
| accelerate | 1.13.0 |
| datasets | 4.8.5 |
| bitsandbytes | 0.49.2 |
| scipy | 1.15.3 |
| wandb | 0.27.0 |
| sentencepiece | 0.2.1 |

### Model Config (Mistral-7B-Instruct-v0.1)
| Field | Value |
|-------|-------|
| rope_theta | **10000.0** |
| d_head (hidden_size / num_attention_heads) | **4096 / 32 = 128** |
| model_type | mistral |
| vocab_size | 32000 |
| num_hidden_layers | 32 |
| num_key_value_heads | 8 (GQA) |
| intermediate_size | 14336 |
| sliding_window | 4096 |
| torch_dtype | bfloat16 |

Model path: `/root/autodl-tmp/.hf_cache/AI-ModelScope/Mistral-7B-Instruct-v0.1` (14 GB, 2 shards)

### Disk Space
| Partition | Size | Used | Available |
|-----------|------|------|-----------|
| / (root) | 30G | 11G | 20G |
| /root/autodl-tmp (data) | 250G | 14G | 237G |

Project directory `/root/tbab_multi_turn/` — 642 MB (subdirs: data/, checkpoints/, logs/, scripts/, eval/).

---
