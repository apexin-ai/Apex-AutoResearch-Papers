#!/bin/bash
set -e
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/autodl-tmp/comm_gate_mas

export HF_HOME=/root/autodl-tmp/.hf_cache
export HF_DATASETS_OFFLINE=1

# vLLM health check
echo "Checking vLLM readiness..."
for i in $(seq 1 30); do
  if curl -s http://127.0.0.1:8001/v1/models | grep -q "Llama"; then
    echo "vLLM ready after ${i} checks"
    break
  fi
  if [ $i -eq 30 ]; then
    echo "FATAL: vLLM not ready after 5 minutes"
    exit 1
  fi
  sleep 10
done

mkdir -p outputs/llama_heuristic_t05

SEEDS=(42 123 456 789 1024)
for seed in "${SEEDS[@]}"; do
  out="outputs/llama_heuristic_t05/seed_${seed}.json"
  if [ -f "$out" ]; then
    completed=$(python3 -c "import json; d=json.load(open('$out')); print(d.get('total_completed',0))")
    if [ "$completed" -gt 100 ]; then
      echo "[t=0.5] seed=$seed already done (completed=$completed), skipping"
      continue
    fi
    echo "[t=0.5] seed=$seed had only $completed completed tasks, re-running"
    mv "$out" "${out}.bak"
  fi
  echo "[t=0.5] Running seed=$seed at $(date)"
  python src/pruning_validation.py \
    --mode online_pruning \
    --config configs/llama_heuristic_gsm8k_t05.yaml \
    --detection-mode heuristic \
    --data-seed $seed \
    --output "$out"
  echo "[t=0.5] Finished seed=$seed at $(date)"
done

echo "=== t=0.5 ALL DONE at $(date) ==="
