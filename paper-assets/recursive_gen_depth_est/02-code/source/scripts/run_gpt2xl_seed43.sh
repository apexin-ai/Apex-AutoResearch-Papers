#!/bin/bash
# GPT-2 XL seed=43 replication: nucleus p=0.95
# Validates depth signal reproducibility across seeds (baseline seed=42, acc=83.3%)
# exp_id: gpt2xl_seed43_001

set -e

if [ -n "${AML_EXP_ID:-}" ]; then
    _aml_exit_handler() { local ec=$?; mkdir -p /tmp/agent-ml-exit; printf "%s|%s\n" "$ec" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" > "/tmp/agent-ml-exit/${AML_EXP_ID}.exit"; }
    trap _aml_exit_handler EXIT
fi

PROJECT_DIR="/root/autodl-tmp/recursive_gen_depth_est"
cd $PROJECT_DIR

source /etc/network_turbo 2>/dev/null || true
export HF_HOME=/root/autodl-tmp/.hf_cache
export HF_HUB_DISABLE_XET=1
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt

if [ -f /root/miniconda3/etc/profile.d/conda.sh ]; then
    source /root/miniconda3/etc/profile.d/conda.sh
    conda activate base
fi

export CUDA_VISIBLE_DEVICES=1

SEED=43
MODEL_PATH="/root/autodl-tmp/models/gpt2-xl"
TARGET_MODULES="c_attn,c_proj"
NUM_SAMPLES=5000
DATA_DIR="data/gpt2xl_seed43"
CKPT_DIR="checkpoints/gpt2xl_seed43"
RESULTS_DIR="results/gpt2xl_seed43"
LOG_FILE="results/gpt2xl_seed43/pipeline.log"

mkdir -p "$DATA_DIR" "$CKPT_DIR" "$RESULTS_DIR" logs

exec > >(tee -a "$LOG_FILE") 2>&1

echo "[$(date)] === GPT-2 XL Seed-43 Replication Pipeline ==="
echo "[$(date)] === Baseline: seed=42, acc=83.3% ==="

cp data/gpt2xl/depth_0.jsonl "$DATA_DIR/depth_0.jsonl"

echo "[$(date)] === Step 1: LoRA finetune on depth_0 (seed=$SEED) ==="
python scripts/lora_finetune.py \
    --input_data "$DATA_DIR/depth_0.jsonl" \
    --output_dir "$CKPT_DIR/lora_depth_0" \
    --model_name "$MODEL_PATH" \
    --model_cache /root/autodl-tmp/.hf_cache \
    --target_modules "$TARGET_MODULES" \
    --seed $SEED \
    --lora_rank 16 \
    --lora_alpha 32 \
    --gpu 0

echo "[$(date)] === Step 2: Generate depth_1 ($NUM_SAMPLES samples) ==="
python scripts/generate_next_depth.py \
    --adapter_dir "$CKPT_DIR/lora_depth_0" \
    --output_path "$DATA_DIR/depth_1.jsonl" \
    --target_depth 1 \
    --model_name "$MODEL_PATH" \
    --model_cache /root/autodl-tmp/.hf_cache \
    --num_samples $NUM_SAMPLES \
    --top_p 0.95 \
    --decoding_strategy nucleus \
    --seed $SEED \
    --gpu 0

echo "[$(date)] === Step 3: LoRA finetune on depth_1 (seed=$SEED) ==="
python scripts/lora_finetune.py \
    --input_data "$DATA_DIR/depth_1.jsonl" \
    --output_dir "$CKPT_DIR/lora_depth_1" \
    --model_name "$MODEL_PATH" \
    --model_cache /root/autodl-tmp/.hf_cache \
    --target_modules "$TARGET_MODULES" \
    --seed $SEED \
    --lora_rank 16 \
    --lora_alpha 32 \
    --gpu 0

echo "[$(date)] === Step 4: Generate depth_2 ($NUM_SAMPLES samples) ==="
python scripts/generate_next_depth.py \
    --adapter_dir "$CKPT_DIR/lora_depth_1" \
    --output_path "$DATA_DIR/depth_2.jsonl" \
    --target_depth 2 \
    --model_name "$MODEL_PATH" \
    --model_cache /root/autodl-tmp/.hf_cache \
    --num_samples $NUM_SAMPLES \
    --top_p 0.95 \
    --decoding_strategy nucleus \
    --seed $SEED \
    --gpu 0

echo "[$(date)] === Step 5: LoRA finetune on depth_2 (seed=$SEED) ==="
python scripts/lora_finetune.py \
    --input_data "$DATA_DIR/depth_2.jsonl" \
    --output_dir "$CKPT_DIR/lora_depth_2" \
    --model_name "$MODEL_PATH" \
    --model_cache /root/autodl-tmp/.hf_cache \
    --target_modules "$TARGET_MODULES" \
    --seed $SEED \
    --lora_rank 16 \
    --lora_alpha 32 \
    --gpu 0

echo "[$(date)] === Step 6: Generate depth_3 ($NUM_SAMPLES samples) ==="
python scripts/generate_next_depth.py \
    --adapter_dir "$CKPT_DIR/lora_depth_2" \
    --output_path "$DATA_DIR/depth_3.jsonl" \
    --target_depth 3 \
    --model_name "$MODEL_PATH" \
    --model_cache /root/autodl-tmp/.hf_cache \
    --num_samples $NUM_SAMPLES \
    --top_p 0.95 \
    --decoding_strategy nucleus \
    --seed $SEED \
    --gpu 0

echo "[$(date)] === Step 7: Feature extraction (d0-d3, 4-class) ==="
python scripts/extract_features.py \
    --data_dir "$DATA_DIR/" \
    --model_path "$MODEL_PATH" \
    --output_path "$RESULTS_DIR/features.jsonl" \
    --gpu 0 \
    --max_depth 3

echo "[$(date)] === Step 8: 5-fold CV RF evaluation ==="
python scripts/eval_second_seed.py \
    --features_path "$RESULTS_DIR/features.jsonl" \
    --output_dir "$RESULTS_DIR/"

echo "[$(date)] === Pipeline complete ==="
echo "Results:"
cat "$RESULTS_DIR/summary.json"
