#!/bin/bash
# SimGate MVP: Phase 0 validation + Phase 1 two-GPU parallel experiment
# GPU 0: strong tasks (boil, melt, change-state-of-matter)
# GPU 1: medium + weak tasks (mix-paint, grow-plant)
#
# Task type names are placeholders — update after Phase 0 confirms exact names.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR/.."

RESULTS_DIR="results/mvp"
mkdir -p "$RESULTS_DIR"

echo "============================================================"
echo "SimGate MVP Experiment Pipeline"
echo "Start: $(date)"
echo "============================================================"

# ---- Phase 0: Validate forking ----
echo ""
echo "[Phase 0] Validating ScienceWorld state forking..."
python src/phase0_validate_forking.py --output "$RESULTS_DIR/phase0_validation.json"

# Check gate
GATE=$(python -c "
import json
with open('$RESULTS_DIR/phase0_validation.json') as f:
    d = json.load(f)
print('PASS' if d['gate_pass'] else 'FAIL')
")

if [ "$GATE" != "PASS" ]; then
    echo "[Phase 0] GATE FAILED — aborting Phase 1"
    echo "Check $RESULTS_DIR/phase0_validation.json for details"
    exit 1
fi
echo "[Phase 0] GATE PASSED"

# ---- Phase 1: 3-way signal detection (two GPUs in parallel) ----
echo ""
echo "[Phase 1] Starting 3-way comparison..."

# Strong tasks on GPU 0
# NOTE: Update task type names after confirming with ScienceWorld API
STRONG_TYPES="boil,melt,change-the-state-of-matter-of"
MEDIUM_WEAK_TYPES="chemistry-mix-paint-secondary-color,grow-plant"

echo "[Phase 1] GPU 0: $STRONG_TYPES"
echo "[Phase 1] GPU 1: $MEDIUM_WEAK_TYPES"

python src/phase1_signal.py \
    --task_types "$STRONG_TYPES" \
    --episodes 20 \
    --gpu_id 0 \
    --max_steps 30 \
    --output_dir "$RESULTS_DIR" \
    > "$RESULTS_DIR/phase1_gpu0.log" 2>&1 &
PID1=$!

python src/phase1_signal.py \
    --task_types "$MEDIUM_WEAK_TYPES" \
    --episodes 20 \
    --gpu_id 1 \
    --max_steps 30 \
    --output_dir "$RESULTS_DIR" \
    > "$RESULTS_DIR/phase1_gpu1.log" 2>&1 &
PID2=$!

echo "[Phase 1] Running... GPU0 PID=$PID1, GPU1 PID=$PID2"
echo "[Phase 1] Logs: $RESULTS_DIR/phase1_gpu0.log, phase1_gpu1.log"

# Wait for both
FAIL=0
wait $PID1 || { echo "[Phase 1] GPU 0 FAILED (exit $?)"; FAIL=1; }
wait $PID2 || { echo "[Phase 1] GPU 1 FAILED (exit $?)"; FAIL=1; }

if [ "$FAIL" -ne 0 ]; then
    echo "[Phase 1] Some jobs failed. Check logs."
    echo "Continuing to analysis with available results..."
fi

# ---- Analysis ----
echo ""
echo "[Analysis] Computing statistics..."
python src/analysis.py --results_dir "$RESULTS_DIR"

echo ""
echo "============================================================"
echo "Pipeline complete: $(date)"
echo "Results: $RESULTS_DIR/"
echo "============================================================"
