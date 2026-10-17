#!/bin/bash
# OLMo-1B 递归生成链流水线
# 用法: bash scripts/run_pipeline_olmo.sh

set -e

# Sentinel for cron monitoring — writes exit code to /tmp/agent-ml-exit/{exp_id}.exit
# Works with both submit_training_job (redundant but harmless) and manual ssh_execute runs
if [ -n "${AML_EXP_ID:-}" ]; then
    _aml_exit_handler() { local ec=$?; mkdir -p /tmp/agent-ml-exit; printf '%s|%s\n' "$ec" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" > "/tmp/agent-ml-exit/${AML_EXP_ID}.exit"; }
    trap _aml_exit_handler EXIT
fi

PROJECT_DIR="/root/autodl-tmp/recursive_gen_depth_est"
cd $PROJECT_DIR

# 环境设置
source /etc/network_turbo 2>/dev/null || true
export HF_HOME=/root/autodl-tmp/.hf_cache
export HF_HUB_DISABLE_XET=1
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt

# conda 环境（aml-train 镜像）
if [ -f /root/miniconda3/etc/profile.d/conda.sh ]; then
    source /root/miniconda3/etc/profile.d/conda.sh
    conda activate base
fi

MODEL_PATH="/root/autodl-tmp/models/olmo-1b"
TARGET_MODULES="q_proj,v_proj"
DATA_DIR="data/olmo"
CKPT_DIR="checkpoints/olmo"

mkdir -p $DATA_DIR $CKPT_DIR

# depth_0 应已有 seed_id，直接复制
cp data/depth_0.jsonl $DATA_DIR/depth_0.jsonl

echo "=== Step 1: LoRA finetune on depth-0 (OLMo-1B) ==="
python scripts/lora_finetune.py \
    --input_data $DATA_DIR/depth_0.jsonl \
    --output_dir $CKPT_DIR/lora_depth_0 \
    --model_name $MODEL_PATH \
    --model_cache /root/autodl-tmp/.hf_cache \
    --target_modules $TARGET_MODULES \
    --gpu 0

echo "=== Step 2: Generate depth-1 ==="
python scripts/generate_next_depth.py \
    --adapter_dir $CKPT_DIR/lora_depth_0 \
    --input_data $DATA_DIR/depth_0.jsonl \
    --output_path $DATA_DIR/depth_1.jsonl \
    --model_name $MODEL_PATH \
    --model_cache /root/autodl-tmp/.hf_cache \
    --target_depth 1 --gpu 0

echo "=== Step 3: LoRA finetune on depth-1 ==="
python scripts/lora_finetune.py \
    --input_data $DATA_DIR/depth_1.jsonl \
    --output_dir $CKPT_DIR/lora_depth_1 \
    --model_name $MODEL_PATH \
    --model_cache /root/autodl-tmp/.hf_cache \
    --target_modules $TARGET_MODULES \
    --gpu 0

echo "=== Step 4: Generate depth-2 ==="
python scripts/generate_next_depth.py \
    --adapter_dir $CKPT_DIR/lora_depth_1 \
    --input_data $DATA_DIR/depth_1.jsonl \
    --output_path $DATA_DIR/depth_2.jsonl \
    --model_name $MODEL_PATH \
    --model_cache /root/autodl-tmp/.hf_cache \
    --target_depth 2 --gpu 0

echo "=== Step 5: LoRA finetune on depth-2 ==="
python scripts/lora_finetune.py \
    --input_data $DATA_DIR/depth_2.jsonl \
    --output_dir $CKPT_DIR/lora_depth_2 \
    --model_name $MODEL_PATH \
    --model_cache /root/autodl-tmp/.hf_cache \
    --target_modules $TARGET_MODULES \
    --gpu 0

echo "=== Step 6: Generate depth-3 ==="
python scripts/generate_next_depth.py \
    --adapter_dir $CKPT_DIR/lora_depth_2 \
    --input_data $DATA_DIR/depth_2.jsonl \
    --output_path $DATA_DIR/depth_3.jsonl \
    --model_name $MODEL_PATH \
    --model_cache /root/autodl-tmp/.hf_cache \
    --target_depth 3 --gpu 0

echo "=== OLMo-1B Pipeline complete! ==="
echo "Data files:"
wc -l $DATA_DIR/depth_*.jsonl
