#!/bin/bash
# P0 PI Sweep: 4x4 Kp/Ki grid on Pythia-1B (16 configs, serial)
# Expected: ~40 GPU-hours on RTX PRO 6000
# submit_training_job timeout: 259200
set -euo pipefail
source /root/collapse-aware-mixing/env_init.sh

# Preflight
[ -f /root/collapse-aware-mixing/controlled_pipeline.py ] || { echo "FAIL: controlled_pipeline.py not found"; exit 1; }
python3 -c "import torch; assert torch.cuda.is_available(), 'No GPU'" || exit 1

cd /root/collapse-aware-mixing

KP_VALUES="0.005 0.01 0.02 0.05"
KI_VALUES="0.002 0.005 0.01 0.02"
BASE_DIR="/root/autodl-tmp/output_p0/pi_sweep"
TOTAL=16
COUNT=0

for KP in $KP_VALUES; do
  for KI in $KI_VALUES; do
    COUNT=$((COUNT + 1))
    OUT_DIR="${BASE_DIR}/kp${KP}_ki${KI}"
    echo "=== [$COUNT/$TOTAL] Kp=$KP Ki=$KI -> $OUT_DIR ==="

    if [ -f "${OUT_DIR}/control_log.jsonl" ]; then
      echo "  SKIP: output already exists"
      continue
    fi

    python3 controlled_pipeline.py \
        --output_dir "$OUT_DIR" \
        --num_generations 3 \
        --tokens_per_generation 20000000 \
        --checkpoint_interval_tokens 5000000 \
        --model_name EleutherAI/pythia-1b \
        --learning_rate 0.000002 \
        --Kp "$KP" --Ki "$KI" \
        --w_init 0.5 \
        --seed 42 \
        --no_wandb

    echo "  DONE: Kp=$KP Ki=$KI"
  done
done

echo "=== All $TOTAL sweep configs complete ==="
echo "=== Running analyze_sweep.py ==="
python3 analyze_sweep.py \
    --sweep-dir "$BASE_DIR" \
    --output "${BASE_DIR}/sweep_report.json"
