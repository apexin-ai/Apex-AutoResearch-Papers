#!/bin/bash
set -e

source /root/miniconda3/etc/profile.d/conda.sh
conda activate base
source /etc/network_turbo

export HF_HOME=/root/autodl-tmp/.hf_cache
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt
export HF_HUB_DISABLE_XET=1
export CUDA_VISIBLE_DEVICES=3

MODEL_DIR=/root/autodl-tmp/models/Qwen/Qwen2.5-3B-Instruct

# Download model if not cached
if [ ! -d "$MODEL_DIR" ] || [ -z "$(ls -A $MODEL_DIR 2>/dev/null)" ]; then
    echo "Downloading Qwen2.5-3B-Instruct via ModelScope..."
    python3 -c "
from modelscope import snapshot_download
snapshot_download('Qwen/Qwen2.5-3B-Instruct', cache_dir='/root/autodl-tmp/models')
print('MODEL_DOWNLOAD_DONE')
"
else
    echo "Model already cached at $MODEL_DIR"
fi

EVAL_SCRIPT=/root/contamcal-irt-calibration/exp001/evaluate.py
RESULTS_BASE=/root/autodl-tmp/exp001/eval_results

# Aligned eval
echo "=== Starting aligned eval ==="
python3 $EVAL_SCRIPT \
    --model-path $MODEL_DIR \
    --output-dir $RESULTS_BASE/Qwen2.5-3B-Instruct_aligned \
    --mc-format aligned \
    --benchmarks mmlu gsm8k arc_challenge humaneval

# Para-aligned eval
echo "=== Starting para_aligned eval ==="
python3 $EVAL_SCRIPT \
    --model-path $MODEL_DIR \
    --output-dir $RESULTS_BASE/Qwen2.5-3B-Instruct_para_aligned \
    --mc-format aligned \
    --paraphrase-dir /root/autodl-tmp/exp001/paraphrases \
    --benchmarks mmlu gsm8k arc_challenge humaneval

echo "=== All evals done ==="
