# ops westd env setup

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd-env-setup_20260518T062747_result.json`
- **Structured JSON:** [`b82fa7b61a3ed480fafe.json`](../../sessions/b8/b82fa7b61a3ed480fafe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 完成报告

### 环境状态 (westd-29999)
| 项目 | 值 |
|------|-----|
| Python | 3.12.3 (conda base) |
| CUDA | 12.8 (nvcc V12.8.93) |
| Driver | 580.82.09 |
| PyTorch | 2.8.0+cu128 |
| GPU | 4× RTX PRO 6000 Blackwell, **96GB** each |
| transformers | 5.8.1 |
| peft | 0.19.1 |
| accelerate | 1.13.0 |
| bitsandbytes | 0.49.2 |
| datasets | 4.8.5 |
| trl | 1.4.0 |
| scipy | 1.17.1 |
| cmdstanpy | 1.3.0 |

### 代码同步
- 从 cqa1-21977 通过 SSH key + scp 传输完成
- 目录: `/root/contamcal-irt-calibration/` (exp001/exp002/exp006/exp008/exp008_new/scripts/stan_models)
- SFT 数据: `/root/autodl-tmp/sft_data/` (5 dosages, 279K samples, 已验证行数一致)
- git 已初始化

### train_sft.py QLoRA 支持
两台服务器均已 patch，新增参数:
- `--load-in-4bit`: 启用 4-bit 量化
- `--bnb-4bit-quant-type {nf4,fp4}`
- `--bnb-4bit-compute-dtype {bfloat16,float16}`

### 配置文件
- `qwen25_14b_qlora.yaml`: QLoRA 4-bit 配置 (适用 <50GB GPU)
- `qwen25_14b_96g.yaml`: bf16 LoRA 配置 (适用 96GB GPU，推荐)

### 重要：GPU VRAM 修正
任务假设 48GB，实际 **96GB**。14B bf16 (~28GB 权重) 不需要 QLoRA，直接 bf16 LoRA + gradient checkpointing 即可。QLoRA 配置已创建但建议优先使用 `qwen25_14b_96g.yaml`。

### Pilot 命令 (7B d000 s42)

```bash
# 激活 conda 环境
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

# Pilot: Qwen2.5-7B d000 s42, cuda:0, bf16 LoRA (96GB 无需 QLoRA)
CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache python3 \
  /root/contamcal-irt-calibration/exp001/train_sft.py \
  --model-name Qwen/Qwen2.5-7B \
  --data-path /root/autodl-tmp/sft_data/sft_dosage_000.jsonl \
  --output-dir /root/autodl-tmp/checkpoints/Qwen2.5-7B_d000_s42 \
  --lora-r 16 --lora-alpha 32 \
  --lr 5e-5 \
  --batch-size 2 \
  --grad-accum 8 \
  --epochs 1 \
  --max-seq-length 2048 \
  --gradient-checkpointing \
  --seed 42
```

14B 版本 (bf16 LoRA，推荐):
```bash
CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache python3 \
  /root/contamcal-irt-calibration/exp001/train_sft.py \
  --model-name Qwen/Qwen2.5-14B \
  --data-path /root/autodl-tmp/sft_data/sft_dosage_000.jsonl \
  --output-dir /root/autodl-tmp/checkpoints/Qwen2.5-14B_d000_s42 \
  --lora-r 16 --lora-alpha 32 \
  --lr 5e-5 \
  --batch-size 2 \
  --grad-accum 8 \
  --epochs 1 \
  --max-seq-length 2048 \
  --gradient-checkpointing \
  --seed 42
```

14B QLoRA 版本 (备选):
```bash
CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache python3 \
  /root/contamcal-irt-calibration/exp001/train_sft.py \
  --model-name Qwen/Qwen2.5-14B \
  --data-path /root/autodl-tmp/sft_data/sft_dosage_000.jsonl \
  --output-dir /root/autodl-tmp/checkpoints/Qwen2.5-14B_d000_qlora_s42 \
  --lora-r 16 --lora-alpha 32 \
  --lr 2e-5 \
  --batch-size 2 \
  --grad-accum 8 \
  --epochs 1 \
  --max-seq-length 2048 \
  --gradient-checkpointing \
  --load-in-4bit \
  --seed 42
```

---
