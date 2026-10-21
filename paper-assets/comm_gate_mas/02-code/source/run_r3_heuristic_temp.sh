#!/bin/bash
set -e
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/autodl-tmp/comm_gate_mas

export HF_HOME=/root/autodl-tmp/.hf_cache
export HF_DATASETS_OFFLINE=1

SEEDS=(42 123 456 789 1024)

echo "=== R3 Llama Heuristic Pruning: Temperature Crossover Study ==="
echo "Start time: $(date)"

# --- Temperature 0.3 ---
echo ""
echo "========== TEMPERATURE 0.3 =========="
for seed in "${SEEDS[@]}"; do
  echo "[t=0.3] Running seed=$seed at $(date)"
  python src/pruning_validation.py \
    --mode online_pruning \
    --config configs/llama_heuristic_gsm8k_t03.yaml \
    --detection-mode heuristic \
    --data-seed $seed \
    --output outputs/llama_heuristic_t03/seed_${seed}.json
  echo "[t=0.3] Finished seed=$seed at $(date)"
done

# --- Temperature 0.5 ---
echo ""
echo "========== TEMPERATURE 0.5 =========="
for seed in "${SEEDS[@]}"; do
  echo "[t=0.5] Running seed=$seed at $(date)"
  python src/pruning_validation.py \
    --mode online_pruning \
    --config configs/llama_heuristic_gsm8k_t05.yaml \
    --detection-mode heuristic \
    --data-seed $seed \
    --output outputs/llama_heuristic_t05/seed_${seed}.json
  echo "[t=0.5] Finished seed=$seed at $(date)"
done

echo ""
echo "=== ALL DONE at $(date) ==="
