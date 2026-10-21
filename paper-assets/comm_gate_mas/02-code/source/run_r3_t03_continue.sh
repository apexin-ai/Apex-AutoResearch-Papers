#!/bin/bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/autodl-tmp/comm_gate_mas
export HF_HOME=/root/autodl-tmp/.hf_cache
export HF_DATASETS_OFFLINE=1

for seed in 42 123; do
  out="outputs/llama_heuristic_t03/seed_${seed}.json"
  echo "[t=0.3] Re-running seed=$seed at $(date)"
  mv "$out" "${out}.bak" 2>/dev/null
  python src/pruning_validation.py \
    --mode online_pruning \
    --config configs/llama_heuristic_gsm8k_t03.yaml \
    --detection-mode heuristic \
    --data-seed $seed \
    --output "$out"
  echo "[t=0.3] Finished seed=$seed at $(date)"
done

echo "=== t=0.3 seed_42 + seed_123 rerun DONE at $(date) ==="
