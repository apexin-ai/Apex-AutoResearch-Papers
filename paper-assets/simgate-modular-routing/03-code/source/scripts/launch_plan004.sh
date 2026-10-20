#!/bin/bash
# Plan-004: Explicit vs Implicit Routing Ablation
#
# Conditions:
#   (a) 1.7B Explicit Router — reuses plan-002 checkpoint, no training needed
#   (b) 1.7B Implicit Router — trains Qwen3-1.7B causal LM with [SIMULATE] prefix
#   (c) 7B Implicit Router  — prompt-only evaluation, no training
#
# Prerequisites: Plan-002 explicit router must be trained first (launch_plan002.sh).
#   If plan-002 adapter is not available, condition (a) is skipped in comparison.
#
# Usage: bash scripts/launch_plan004.sh

set -euo pipefail

source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/autodl-tmp/simgate-modular-routing

# AutoDL network acceleration
source /etc/network_turbo 2>/dev/null || true
export HF_HOME=/root/autodl-tmp/.hf_cache
export HF_HUB_DISABLE_XET=1
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt

# Local model paths (already downloaded)
QWEN3_1_7B="/root/autodl-tmp/models/Qwen/Qwen3-1.7B"
QWEN2_5_7B="/root/autodl-tmp/models/Qwen/Qwen2.5-7B-Instruct"
PLAN002_ADAPTER="results/plan_002_router/final_adapter"

echo "=========================================="
echo " Plan-004: Explicit vs Implicit Routing"
echo "=========================================="

# ──────────────────────────────────────────────
# Step 1: Format data for implicit routing (condition b)
# ──────────────────────────────────────────────
echo ""
echo "[Step 1] Formatting implicit SFT data..."
python src/training/format_implicit_data.py \
    --data_dir results/plan_c \
    --output_dir data/plan-004-implicit

# ──────────────────────────────────────────────
# Step 2: Train implicit router (condition b)
# Uses GPU 1 to avoid conflict with other jobs
# ──────────────────────────────────────────────
echo ""
echo "[Step 2] Training 1.7B Implicit Router..."
CUDA_VISIBLE_DEVICES=1 python src/training/implicit_router_sft.py train \
    --data_dir data/plan-004-implicit \
    --model_name "${QWEN3_1_7B}" \
    --output_dir checkpoints/plan-004-implicit \
    --lr 2e-5 \
    --batch_size 32 \
    --epochs 3 \
    --max_seq_len 2048 \
    --seed 42

# ──────────────────────────────────────────────
# Step 3: Evaluate all three conditions
# ──────────────────────────────────────────────
echo ""
echo "[Step 3] Running three-condition comparison..."

COMPARISON_ARGS=(
    --run_live
    --implicit_ckpt checkpoints/plan-004-implicit/final_adapter
    --prompt_model "${QWEN2_5_7B}"
    --data_dir results/plan_c
    --output_dir results/plan-004-ablation
    --oracle_data results/sft_data_death_aware/sft_triples.jsonl
)

# Include explicit router if plan-002 adapter exists
if [ -d "${PLAN002_ADAPTER}" ]; then
    COMPARISON_ARGS+=(--explicit_ckpt "${PLAN002_ADAPTER}")
    echo "  Plan-002 adapter found, including condition (a)."
else
    echo "  Plan-002 adapter not found at ${PLAN002_ADAPTER}, skipping condition (a)."
fi

python src/evaluation/ablation_comparison.py "${COMPARISON_ARGS[@]}"

echo ""
echo "=========================================="
echo " Plan-004 complete!"
echo " Results: results/plan-004-ablation/"
echo "=========================================="
