#!/bin/bash
set -e

cd .
source $CONDA_PREFIX/etc/profile.d/conda.sh && conda activate base
export PYTHONPATH=.:$PYTHONPATH
export CUDA_VISIBLE_DEVICES=0
export VLLM_USE_V1=0

echo "=== exp-002 pilot start: $(date) ==="

# MMLU (10 conditions × 200 items = 2000 records)
echo ""
echo "=== MMLU pilot: $(date) ==="
python -m src.inference.run_experiment \
  --design results/exp002_pilot/pilot_design_mmlu.csv \
  --items data/mmlu_items_exp001.json \
  --benchmark mmlu \
  --gpu-id 0 \
  --output results/exp002_pilot/mmlu_pilot.jsonl

# GSM8K (10 conditions × 200 items = 2000 records, max_tokens=512 auto)
echo ""
echo "=== GSM8K pilot: $(date) ==="
python -m src.inference.run_experiment \
  --design results/exp002_pilot/pilot_design_gsm8k.csv \
  --benchmark gsm8k \
  --gpu-id 0 \
  --output results/exp002_pilot/gsm8k_pilot.jsonl

# ARC (10 conditions × 200 items = 2000 records)
echo ""
echo "=== ARC pilot: $(date) ==="
python -m src.inference.run_experiment \
  --design results/exp002_pilot/pilot_design_arc.csv \
  --benchmark arc \
  --gpu-id 0 \
  --output results/exp002_pilot/arc_pilot.jsonl

# HellaSwag (10 conditions × 200 items = 2000 records)
echo ""
echo "=== HellaSwag pilot: $(date) ==="
python -m src.inference.run_experiment \
  --design results/exp002_pilot/pilot_design_hellaswag.csv \
  --benchmark hellaswag \
  --gpu-id 0 \
  --output results/exp002_pilot/hellaswag_pilot.jsonl

echo ""
echo "=== exp-002 pilot complete: $(date) ==="
echo "PILOT_DONE"
