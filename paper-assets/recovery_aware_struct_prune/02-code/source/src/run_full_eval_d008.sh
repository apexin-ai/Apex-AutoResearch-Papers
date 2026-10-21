#!/bin/bash
# D008 Full GSM8K eval (1319 samples) for all 4 models
# Serial version: bash src/run_full_eval_d008.sh [gpu_id]
# ~2h per eval, ~8h total

set -euo pipefail
GPU=${1:-0}
cd /root/recovery_aware_struct_prune
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

echo "=== [1/4] Post-prune RASP 20% (full 1319) ==="
CUDA_VISIBLE_DEVICES=$GPU python src/eval_gsm8k.py \
    --model_path /root/autodl-tmp/pruned_rasp_20 \
    --max_new_tokens 4096 \
    --output_path results/eval_pruned_rasp_20_full.json

echo "=== [2/4] Post-prune Standard 20% (full 1319) ==="
CUDA_VISIBLE_DEVICES=$GPU python src/eval_gsm8k.py \
    --model_path /root/autodl-tmp/pruned_standard_20 \
    --max_new_tokens 4096 \
    --output_path results/eval_pruned_standard_20_full.json

echo "=== [3/4] Post-recovery RASP 20% (full 1319) ==="
RECOVERED_RASP="/root/autodl-tmp/recovered_rasp_20"
LATEST_CKPT=$(ls -d ${RECOVERED_RASP}/checkpoint-* 2>/dev/null | sort -t- -k2 -n | tail -1)
[ -z "$LATEST_CKPT" ] && LATEST_CKPT="$RECOVERED_RASP"
echo "Using checkpoint: $LATEST_CKPT"
CUDA_VISIBLE_DEVICES=$GPU python src/eval_gsm8k.py \
    --model_path "$LATEST_CKPT" \
    --max_new_tokens 4096 \
    --output_path results/eval_recovered_rasp_20_full.json

echo "=== [4/4] Post-recovery Standard 20% (full 1319) ==="
RECOVERED_STD="/root/autodl-tmp/recovered_standard_20"
LATEST_CKPT=$(ls -d ${RECOVERED_STD}/checkpoint-* 2>/dev/null | sort -t- -k2 -n | tail -1)
[ -z "$LATEST_CKPT" ] && LATEST_CKPT="$RECOVERED_STD"
echo "Using checkpoint: $LATEST_CKPT"
CUDA_VISIBLE_DEVICES=$GPU python src/eval_gsm8k.py \
    --model_path "$LATEST_CKPT" \
    --max_new_tokens 4096 \
    --output_path results/eval_recovered_standard_20_full.json

echo "=== All 4 evals done ==="
