#!/bin/bash
set -e
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/autodl-tmp/comm_gate_mas

export HF_HOME=/root/autodl-tmp/.hf_cache
export HF_DATASETS_OFFLINE=1

# vLLM health check (port 8002)
echo "Checking vLLM on port 8002..."
for i in $(seq 1 30); do
  if curl -s http://127.0.0.1:8002/v1/models | grep -q "Llama"; then
    echo "vLLM (cuda:1) ready after ${i} checks"
    break
  fi
  if [ $i -eq 30 ]; then
    echo "FATAL: vLLM on port 8002 not ready after 5 minutes"
    exit 1
  fi
  sleep 10
done

# === Part 1: t=0.3 seeds 789, 1024 ===
mkdir -p outputs/llama_heuristic_t03

for seed in 789 1024; do
  out="outputs/llama_heuristic_t03/seed_${seed}.json"
  if [ -f "$out" ]; then
    completed=$(python3 -c "import json; d=json.load(open('$out')); print(d.get('total_completed',0))")
    if [ "$completed" -gt 100 ]; then
      echo "[t=0.3][cuda1] seed=$seed already done (completed=$completed), skipping"
      continue
    fi
    echo "[t=0.3][cuda1] seed=$seed had only $completed completed, re-running"
    mv "$out" "${out}.bak"
  fi
  echo "[t=0.3][cuda1] Running seed=$seed at $(date)"
  python src/pruning_validation.py \
    --mode online_pruning \
    --config configs/llama_heuristic_gsm8k_t03_cuda1.yaml \
    --detection-mode heuristic \
    --data-seed $seed \
    --output "$out"
  echo "[t=0.3][cuda1] Finished seed=$seed at $(date)"
done

echo "=== t=0.3 cuda1 DONE at $(date) ==="

# === Part 2: t=0.5 seeds 456, 789, 1024 ===
mkdir -p outputs/llama_heuristic_t05

for seed in 456 789 1024; do
  out="outputs/llama_heuristic_t05/seed_${seed}.json"
  if [ -f "$out" ]; then
    completed=$(python3 -c "import json; d=json.load(open('$out')); print(d.get('total_completed',0))")
    if [ "$completed" -gt 100 ]; then
      echo "[t=0.5][cuda1] seed=$seed already done (completed=$completed), skipping"
      continue
    fi
    echo "[t=0.5][cuda1] seed=$seed had only $completed completed, re-running"
    mv "$out" "${out}.bak"
  fi
  echo "[t=0.5][cuda1] Running seed=$seed at $(date)"
  python src/pruning_validation.py \
    --mode online_pruning \
    --config configs/llama_heuristic_gsm8k_t05_cuda1.yaml \
    --detection-mode heuristic \
    --data-seed $seed \
    --output "$out"
  echo "[t=0.5][cuda1] Finished seed=$seed at $(date)"
done

echo "=== ALL cuda1 work DONE at $(date) ==="
