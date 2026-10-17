#!/bin/bash
# 递归生成链流水线 (OLMo-1B, top_k=50)

set -e

# Sentinel for cron monitoring — writes exit code to /tmp/agent-ml-exit/{exp_id}.exit
# Works with both submit_training_job (redundant but harmless) and manual ssh_execute runs
if [ -n "${AML_EXP_ID:-}" ]; then
    _aml_exit_handler() { local ec=$?; mkdir -p /tmp/agent-ml-exit; printf '%s|%s\n' "$ec" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" > "/tmp/agent-ml-exit/${AML_EXP_ID}.exit"; }
    trap _aml_exit_handler EXIT
fi

PROJECT_DIR="/root/autodl-tmp/recursive_gen_depth_est"
cd $PROJECT_DIR

GPU=${GPU:-0}
DATA_DIR="data/olmo_topk50"
CKPT_DIR="checkpoints/olmo_topk50"
LOG_FILE="logs/pipeline_olmo_topk50.log"

source /etc/network_turbo 2>/dev/null || true
export HF_HOME=/root/autodl-tmp/.hf_cache
export HF_HUB_DISABLE_XET=1
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt

if [ -f /root/miniconda3/etc/profile.d/conda.sh ]; then
    source /root/miniconda3/etc/profile.d/conda.sh
    conda activate base
fi

MODEL_PATH="/root/autodl-tmp/models/olmo-1b-hf"
TARGET_MODULES="q_proj,k_proj,v_proj"

mkdir -p "$DATA_DIR" "$CKPT_DIR" logs

exec > >(tee -a "$LOG_FILE") 2>&1

echo "=== Pipeline: OLMo-1B topk k=50 ==="
echo "=== Started at $(date) ==="
echo "=== GPU: $GPU ==="

# Step 1 skipped: depth-0 adapter is decoding-strategy-independent, reuse nucleus version
NUCLEUS_ADAPTER="/root/autodl-tmp/recursive_gen_depth_est/checkpoints/olmo/lora_depth_0"
if [ ! -d "$NUCLEUS_ADAPTER" ]; then
    echo "ERROR: nucleus depth-0 adapter not found at $NUCLEUS_ADAPTER" >&2
    exit 1
fi
ln -sfn "$NUCLEUS_ADAPTER" "$CKPT_DIR/lora_depth_0"
echo "=== Step 1: Reusing nucleus depth-0 adapter via symlink ==="

echo "=== Step 2: Generate depth-1 ==="
python scripts/generate_next_depth.py \
    --adapter_dir "$CKPT_DIR/lora_depth_0" \
    --output_path "$DATA_DIR/depth_1.jsonl" \
    --target_depth 1 \
    --model_name "$MODEL_PATH" \
    --decoding_strategy topk \
    --top_k 50 \
    --gpu $GPU

echo "=== Step 3: LoRA finetune on depth-1 ==="
python scripts/lora_finetune.py \
    --input_data "$DATA_DIR/depth_1.jsonl" \
    --output_dir "$CKPT_DIR/lora_depth_1" \
    --model_name "$MODEL_PATH" \
    --target_modules "$TARGET_MODULES" \
    --gpu $GPU

echo "=== Step 4: Generate depth-2 ==="
python scripts/generate_next_depth.py \
    --adapter_dir "$CKPT_DIR/lora_depth_1" \
    --output_path "$DATA_DIR/depth_2.jsonl" \
    --target_depth 2 \
    --model_name "$MODEL_PATH" \
    --decoding_strategy topk \
    --top_k 50 \
    --gpu $GPU

echo "=== Step 5: LoRA finetune on depth-2 ==="
python scripts/lora_finetune.py \
    --input_data "$DATA_DIR/depth_2.jsonl" \
    --output_dir "$CKPT_DIR/lora_depth_2" \
    --model_name "$MODEL_PATH" \
    --target_modules "$TARGET_MODULES" \
    --gpu $GPU

echo "=== Step 6: Generate depth-3 ==="
python scripts/generate_next_depth.py \
    --adapter_dir "$CKPT_DIR/lora_depth_2" \
    --output_path "$DATA_DIR/depth_3.jsonl" \
    --target_depth 3 \
    --model_name "$MODEL_PATH" \
    --decoding_strategy topk \
    --top_k 50 \
    --gpu $GPU

echo "=== OLMo-1B topk Pipeline complete! ==="
wc -l "$DATA_DIR"/depth_*.jsonl
echo "=== Finished at $(date) ==="
