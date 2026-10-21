#!/bin/bash
set -e

cd /root/autodl-tmp/comm_gate_mas
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
source /etc/network_turbo 2>/dev/null || true

export CUDA_VISIBLE_DEVICES=2
export HF_DATASETS_OFFLINE=1
export HF_HOME=/root/autodl-tmp/.hf_cache

echo "=========================================="
echo "Prompt Sensitivity Experiment — Llama×GSM8K"
echo "Start: $(date)"
echo "=========================================="

# V1: baseline prompt
echo ""
echo "[$(date)] === V1: Baseline prompt ==="
python src/pruning_validation.py \
  --mode online_pruning \
  --config configs/prompt_sensitivity_v1_baseline.yaml \
  --num-tasks 100 \
  --detection-mode heuristic \
  --data-seed 42 \
  --domain gsm8k \
  --output outputs/prompt_sensitivity/variant_v1.json

echo "[$(date)] V1 done."

# V2: minimal prompt
echo ""
echo "[$(date)] === V2: Minimal prompt ==="
python src/pruning_validation.py \
  --mode online_pruning \
  --config configs/prompt_sensitivity_v2_minimal.yaml \
  --num-tasks 100 \
  --detection-mode heuristic \
  --data-seed 42 \
  --domain gsm8k \
  --output outputs/prompt_sensitivity/variant_v2.json

echo "[$(date)] V2 done."

# V3: verbose prompt
echo ""
echo "[$(date)] === V3: Verbose prompt ==="
python src/pruning_validation.py \
  --mode online_pruning \
  --config configs/prompt_sensitivity_v3_verbose.yaml \
  --num-tasks 100 \
  --detection-mode heuristic \
  --data-seed 42 \
  --domain gsm8k \
  --output outputs/prompt_sensitivity/variant_v3.json

echo "[$(date)] V3 done."

echo ""
echo "=========================================="
echo "All 3 variants complete: $(date)"
echo "=========================================="
