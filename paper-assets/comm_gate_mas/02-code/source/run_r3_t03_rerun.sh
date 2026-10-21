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

# Wait for seed_456 to finish if still running
while ps -p 88421 > /dev/null 2>&1; do
  echo "Waiting for seed_456 (PID 88421) to finish... $(date)"
  sleep 30
done
echo "seed_456 done, starting remaining t=0.3 seeds"

mkdir -p outputs/llama_heuristic_t03

SEEDS=(789 1024 42 123)
for seed in "${SEEDS[@]}"; do
  out="outputs/llama_heuristic_t03/seed_${seed}.json"
  if [ -f "$out" ]; then
    # Check if existing output is a failure (all infra errors)
    completed=$(python3 -c "import json; d=json.load(open('$out')); print(d.get('total_completed',0))")
    if [ "$completed" -gt 100 ]; then
      echo "[t=0.3] seed=$seed already done (completed=$completed), skipping"
      continue
    fi
    echo "[t=0.3] seed=$seed had only $completed completed tasks, re-running"
    mv "$out" "${out}.bak"
  fi
  echo "[t=0.3] Running seed=$seed at $(date)"
  python src/pruning_validation.py \
    --mode online_pruning \
    --config configs/llama_heuristic_gsm8k_t03.yaml \
    --detection-mode heuristic \
    --data-seed $seed \
    --output "$out"
  echo "[t=0.3] Finished seed=$seed at $(date)"
done

echo "=== t=0.3 ALL DONE at $(date) ==="
