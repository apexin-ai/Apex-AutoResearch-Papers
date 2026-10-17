#!/bin/bash
# 递归生成链流水线
# 用法: bash scripts/run_pipeline.sh
#
# 流程: depth-0 → LoRA微调 → 生成depth-1 → LoRA微调 → 生成depth-2 → LoRA微调 → 生成depth-3

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

mkdir -p data checkpoints

echo "=== Step 0: Add seed_id to depth_0 ==="
python scripts/add_seed_id.py

echo "=== Step 1: LoRA finetune on depth-0 ==="
python scripts/lora_finetune.py --input_data data/depth_0.jsonl --output_dir checkpoints/lora_depth_0 --gpu 0

echo "=== Step 2: Generate depth-1 ==="
python scripts/generate_next_depth.py --adapter_dir checkpoints/lora_depth_0 --input_data data/depth_0.jsonl --output_path data/depth_1.jsonl --target_depth 1 --gpu 0

echo "=== Step 3: LoRA finetune on depth-1 ==="
python scripts/lora_finetune.py --input_data data/depth_1.jsonl --output_dir checkpoints/lora_depth_1 --gpu 0

echo "=== Step 4: Generate depth-2 ==="
python scripts/generate_next_depth.py --adapter_dir checkpoints/lora_depth_1 --input_data data/depth_1.jsonl --output_path data/depth_2.jsonl --target_depth 2 --gpu 0

echo "=== Step 5: LoRA finetune on depth-2 ==="
python scripts/lora_finetune.py --input_data data/depth_2.jsonl --output_dir checkpoints/lora_depth_2 --gpu 0

echo "=== Step 6: Generate depth-3 ==="
python scripts/generate_next_depth.py --adapter_dir checkpoints/lora_depth_2 --input_data data/depth_2.jsonl --output_path data/depth_3.jsonl --target_depth 3 --gpu 0

echo "=== Pipeline complete! ==="
echo "Data files:"
wc -l data/depth_*.jsonl
