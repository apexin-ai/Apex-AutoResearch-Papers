#!/bin/bash
# Rerun missing seeds 5120 and 6144 for Qwen 10-seed oracle experiment
# Runs locally, connects to vLLM via SSH tunnel (port 8000)
set -euo pipefail

if [ -z "${OPENAI_API_KEY:[REDACTED]}" ]; then
  echo "FATAL: OPENAI_API_KEY not set in environment"
  exit 1
fi

cd /Users/agent-001/.agent-ml-research/projects/comm_gate_mas

SEEDS=(5120 6144)
for SEED in "${SEEDS[@]}"; do
  OUTFILE="outputs/oracle_qwen_10run/seed_${SEED}.json"
  if [ -f "$OUTFILE" ]; then
    echo "[skip] seed=$SEED already exists: $OUTFILE"
    continue
  fi
  echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) Starting seed=$SEED"
  python3 src/pruning_validation.py \
    --mode online_oracle \
    --config configs/oracle_qwen_gsm8k_10run.yaml \
    --detection-mode oracle_5class \
    --num-tasks 200 \
    --data-seed $SEED \
    --output "$OUTFILE" \
    2>&1 | tee -a outputs/oracle_qwen_10run/run_seed_${SEED}.log
  echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) Finished seed=$SEED"
done
echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) MISSING SEEDS COMPLETE"
