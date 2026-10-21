#!/bin/bash
# TOST experiment: Qwen 10 seeds × N=200, oracle_5class, greedy decoding
# Requires OPENAI_API_KEY in environment

set -euo pipefail

if [ -z "${OPENAI_API_KEY:[REDACTED]}" ]; then
  echo "FATAL: OPENAI_API_KEY not set in environment"
  exit 1
fi

cd /Users/agent-001/.agent-ml-research/projects/comm_gate_mas

LOCKFILE="outputs/oracle_qwen_10run/.lock"
if [ -f "$LOCKFILE" ]; then
  OLD_PID=$(cat "$LOCKFILE")
  if kill -0 "$OLD_PID" 2>/dev/null; then
    echo "FATAL: Another instance already running (PID=$OLD_PID). Aborting."
    exit 1
  fi
  echo "WARNING: Stale lockfile (PID=$OLD_PID dead), removing"
  rm -f "$LOCKFILE"
fi
echo $$ > "$LOCKFILE"
trap 'rm -f "$LOCKFILE"' EXIT

SEEDS=(42 123 456 789 1024 2048 3072 4096 5120 6144)
for SEED in "${SEEDS[@]}"; do
  echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) Starting seed=$SEED"
  python3 src/pruning_validation.py \
    --mode online_oracle \
    --config configs/oracle_qwen_gsm8k_10run.yaml \
    --detection-mode oracle_5class \
    --num-tasks 200 \
    --data-seed $SEED \
    --output outputs/oracle_qwen_10run/seed_${SEED}.json \
    2>&1 | tee -a outputs/oracle_qwen_10run/run_seed_${SEED}.log
  EXIT_CODE=$?
  echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) Finished seed=$SEED, exit=$EXIT_CODE"
  if [ $EXIT_CODE -ne 0 ]; then
    echo "FATAL: seed=$SEED failed with exit=$EXIT_CODE, aborting"
    exit 1
  fi
done
echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) ALL 10 SEEDS COMPLETE"
