# Manual Deployment Guide — Schema-Conformance IE Training

Target: seetacloud-westb-2xpro6000 (2x RTX PRO 6000 96GB)

## 1. SSH Connect

```bash
ssh seetacloud-westb-2xpro6000
```

## 2. Environment Detection

```bash
which python3 && python3 --version
nvidia-smi --query-gpu=name,memory.total,driver_version --format=csv,noheader
nvcc --version 2>/dev/null | grep "release"
ls -d /root/miniconda3 .venv 2>/dev/null
pip3 list --format=freeze 2>/dev/null | grep -iE "torch|transformers|flash"
```

## 3. Clone / Sync Code

```bash
cd /root/autodl-tmp
git clone <REPO_URL> schema-conform-ie-training
cd schema-conform-ie-training/code
```

Or if already cloned:
```bash
cd /root/autodl-tmp/schema-conform-ie-training/code
git pull
```

## 4. Python Environment

If conda (aml-train image):
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
```

If no conda:
```bash
python3 -m venv .venv && source .venv/bin/activate
```

## 5. Install Dependencies

```bash
# PyTorch (adjust cu124 to match your CUDA version)
pip install --timeout 300 torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124

# Project deps
pip install --timeout 300 -r requirements.txt

# flash-attn (optional, speeds up training)
pip install flash-attn --no-build-isolation
```

## 6. Verify GPU

```bash
python -c "
import torch
print(f'torch={torch.__version__}, cuda={torch.cuda.is_available()}, gpus={torch.cuda.device_count()}')
for i in range(torch.cuda.device_count()):
    p = torch.cuda.get_device_properties(i)
    print(f'  GPU {i}: {torch.cuda.get_device_name(i)} ({p.total_mem // 1024**3}GB)')
"
```

Expected: 2x RTX PRO 6000, 96GB each.

## 7. Download Model

```bash
export HF_HOME=/root/autodl-tmp/.hf_cache
export HF_HUB_DISABLE_XET=1

# AutoDL: enable proxy first
source /etc/network_turbo 2>/dev/null
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt

python -c "
from transformers import AutoTokenizer, AutoModelForCausalLM
AutoTokenizer.from_pretrained('Qwen/Qwen3.5-9B', trust_remote_code=True)
AutoModelForCausalLM.from_pretrained('Qwen/Qwen3.5-9B', trust_remote_code=True)
print('Done.')
"
```

If HuggingFace is slow on AutoDL, use ModelScope:
```bash
pip install modelscope
python -c "from modelscope import snapshot_download; snapshot_download('Qwen/Qwen3.5-9B', cache_dir='/root/autodl-tmp/.hf_cache')"
```

## 8. Prepare ACE2005 Data

ACE2005 requires LDC license (LDC2006T06). After obtaining, preprocess with DyGIE++:
```bash
# See https://github.com/dwadden/dygiepp for preprocessing
# Expected output: data/ace2005/{train,dev,test}.json (DyGIE++ format)
```

## 9. Dry-Run (5 steps)

```bash
cd /root/autodl-tmp/schema-conform-ie-training/code

CUDA_VISIBLE_DEVICES=0 python -m src.train_grpo \
    --config configs/grpo_baseline.yaml \
    --data_dir /path/to/ace2005 \
    --output_dir ./output/dry_run \
    --dry_run
```

## 10. Start Training

Two GPUs, two groups, in parallel:

```bash
# Terminal 1 — Group A: F1 only (cuda:0)
CUDA_VISIBLE_DEVICES=0 python -m src.train_grpo \
    --config configs/grpo_baseline.yaml \
    --data_dir /path/to/ace2005 \
    --output_dir ./output/grpo_baseline

# Terminal 2 — Group B: conformance + GDPO (cuda:1)
CUDA_VISIBLE_DEVICES=1 python -m src.train_grpo \
    --config configs/grpo_conformance.yaml \
    --data_dir /path/to/ace2005 \
    --output_dir ./output/grpo_conformance
```

Using tmux (recommended):
```bash
mkdir -p logs

tmux new-session -d -s grpA "CUDA_VISIBLE_DEVICES=0 python -m src.train_grpo --config configs/grpo_baseline.yaml --data_dir /path/to/ace2005 --output_dir ./output/grpo_baseline 2>&1 | tee logs/groupA.log"

tmux new-session -d -s grpB "CUDA_VISIBLE_DEVICES=1 python -m src.train_grpo --config configs/grpo_conformance.yaml --data_dir /path/to/ace2005 --output_dir ./output/grpo_conformance 2>&1 | tee logs/groupB.log"
```

## 11. Monitor

```bash
# GPU utilization
watch -n 5 nvidia-smi

# Training logs
tail -f logs/groupA.log
tail -f logs/groupB.log

# W&B: check wandb.ai project "schema-conform-ie"
```

## 12. Evaluate

After training completes:
```bash
# Group A
python -m src.evaluate \
    --model_path ./output/grpo_baseline \
    --eval_datasets ace2005_test crossner_politics crossner_science \
    --data_dir /path/to/data

# Group B
python -m src.evaluate \
    --model_path ./output/grpo_conformance \
    --eval_datasets ace2005_test crossner_politics crossner_science \
    --data_dir /path/to/data

# Group C (base model)
python -m src.inference_base \
    --model_name Qwen/Qwen3.5-9B \
    --eval_datasets ace2005_test crossner_politics crossner_science \
    --data_dir /path/to/data
```
