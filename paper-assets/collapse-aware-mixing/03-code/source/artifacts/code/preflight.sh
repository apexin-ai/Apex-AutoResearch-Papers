#!/bin/bash
set -e
FAIL=0
echo "=== Pre-flight Check ==="

# 1. Python/conda
python3 --version || { echo "FAIL: python3 not found (conda not activated?)"; FAIL=1; }

# 2. GPU
python3 -c "import torch; assert torch.cuda.is_available(), 'No GPU'" || { echo "FAIL: GPU not available"; FAIL=1; }

# 3. GPU no stale processes
GPU_PROCS=$(nvidia-smi --query-compute-apps=pid --format=csv,noheader 2>/dev/null | wc -l)
[ "$GPU_PROCS" -eq 0 ] || { echo "FAIL: $GPU_PROCS processes on GPU, clean up first"; FAIL=1; }

# 4. Dataset cache (wikitext-103-raw-v1)
python3 -c "from datasets import load_dataset; ds = load_dataset('wikitext', 'wikitext-103-raw-v1', cache_dir='$HF_HOME/datasets'); assert len(ds['train']) > 10000, f'Only {len(ds[\"train\"])} docs'" || { echo "FAIL: wikitext cache incomplete"; FAIL=1; }

# 5. Model cache
python3 -c "from transformers import AutoModelForCausalLM, AutoTokenizer; AutoTokenizer.from_pretrained('EleutherAI/pythia-1b', cache_dir='$HF_HOME'); AutoModelForCausalLM.from_pretrained('EleutherAI/pythia-1b', cache_dir='$HF_HOME', torch_dtype='auto')" || { echo "FAIL: Pythia-1B cache incomplete"; FAIL=1; }

# 6. Data disk space
AVAIL=$(df /root/autodl-tmp --output=avail -BG | tail -1 | tr -d 'G ')
[ "$AVAIL" -gt 50 ] || { echo "FAIL: /root/autodl-tmp only ${AVAIL}GB free (need >50GB)"; FAIL=1; }

# 7. Root partition
ROOT_AVAIL=$(df / --output=avail -BG | tail -1 | tr -d 'G ')
[ "$ROOT_AVAIL" -gt 5 ] || { echo "FAIL: / only ${ROOT_AVAIL}GB free (need >5GB)"; FAIL=1; }

# 8. Stale locks
STALE_LOCKS=$(find "$HF_HOME" -name "*.lock" -mmin +30 2>/dev/null | wc -l)
[ "$STALE_LOCKS" -eq 0 ] || { echo "WARN: $STALE_LOCKS stale lock files found, cleaning..."; find "$HF_HOME" -name "*.lock" -mmin +30 -delete; }

echo "=== Pre-flight $([ $FAIL -eq 0 ] && echo 'PASSED' || echo 'FAILED') ==="
exit $FAIL
