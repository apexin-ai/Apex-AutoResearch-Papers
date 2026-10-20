#!/bin/bash
# P0 Seed Validation: PI controller vs best fixed ratio, 3 seeds each
# Expected: ~30 GPU-hours on RTX PRO 6000
# submit_training_job timeout: 259200
#
# Usage: BEST_RATIO=0.5 bash launch_seed_validation_p0.sh
#   Set BEST_RATIO to the best fixed ratio from baseline results before running.
set -euo pipefail
source /root/collapse-aware-mixing/env_init.sh

# Preflight
[ -f /root/collapse-aware-mixing/controlled_pipeline.py ] || { echo "FAIL: controlled_pipeline.py not found"; exit 1; }
python3 -c "import torch; assert torch.cuda.is_available(), 'No GPU'" || exit 1

cd /root/collapse-aware-mixing

BEST_RATIO=${BEST_RATIO:?"ERROR: Set BEST_RATIO env var to the best fixed ratio (e.g. BEST_RATIO=0.5)"}
SEEDS="42 123 456"
BASE_DIR="/root/autodl-tmp/output_p0/seed_validation"
TOTAL=6
COUNT=0

for SEED in $SEEDS; do
  # --- PI controller ---
  COUNT=$((COUNT + 1))
  PI_DIR="${BASE_DIR}/output_seed_${SEED}_pi"
  echo "=== [$COUNT/$TOTAL] PI controller, seed=$SEED ==="

  if [ -f "${PI_DIR}/control_log.jsonl" ]; then
    echo "  SKIP: output already exists"
  else
    python3 controlled_pipeline.py \
        --output_dir "$PI_DIR" \
        --num_generations 3 \
        --tokens_per_generation 20000000 \
        --checkpoint_interval_tokens 5000000 \
        --model_name EleutherAI/pythia-1b \
        --learning_rate 0.000002 \
        --Kp 0.01 --Ki 0.005 \
        --w_init 0.5 \
        --seed "$SEED" \
        --no_wandb
    echo "  DONE: PI seed=$SEED"
  fi

  # --- Fixed ratio ---
  COUNT=$((COUNT + 1))
  FIX_DIR="${BASE_DIR}/output_seed_${SEED}_fixed"
  echo "=== [$COUNT/$TOTAL] Fixed ratio=$BEST_RATIO, seed=$SEED ==="

  if [ -f "${FIX_DIR}/control_log.jsonl" ]; then
    echo "  SKIP: output already exists"
  else
    python3 controlled_pipeline.py \
        --output_dir "$FIX_DIR" \
        --num_generations 3 \
        --tokens_per_generation 20000000 \
        --checkpoint_interval_tokens 5000000 \
        --model_name EleutherAI/pythia-1b \
        --learning_rate 0.000002 \
        --Kp 0 --Ki 0 \
        --w_init "$BEST_RATIO" --w_min "$BEST_RATIO" --w_max "$BEST_RATIO" \
        --seed "$SEED" \
        --no_wandb
    echo "  DONE: Fixed seed=$SEED"
  fi
done

echo "=== All $TOTAL seed validation runs complete ==="
echo "=== Running analyze_seed_validation.py ==="
python3 analyze_seed_validation.py \
    --base-dir "$BASE_DIR" \
    --seeds 42 123 456 \
    --output "${BASE_DIR}/seed_validation_report.json"
