#!/usr/bin/env bash
# exp-005: Noise Propagation Simulation
# Verifies ME model propagates exposure noise into CI width
#
# Usage:
#   bash run_exp005.sh
#   N_SEEDS=3 bash run_exp005.sh  # quick test

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
OUTPUT_DIR="${OUTPUT_DIR:-/root/contamcal-irt-calibration/results/exp005}"
STAN_ME="${STAN_ME:-${SCRIPT_DIR}/../exp006_irt_calibration/contam_irt_4pl_me.stan}"
STAN_SIMPLE="${STAN_SIMPLE:-${SCRIPT_DIR}/../exp006_irt_calibration/contam_irt_4pl_simple.stan}"
N_SEEDS="${N_SEEDS:-5}"
N_MODELS="${N_MODELS:-30}"
N_ITEMS="${N_ITEMS:-300}"

mkdir -p "$OUTPUT_DIR"

echo "=== exp-005: Noise Propagation Simulation ==="
echo "Output dir:   $OUTPUT_DIR"
echo "Stan ME:      $STAN_ME"
echo "Stan simple:  $STAN_SIMPLE"
echo "Seeds/level:  $N_SEEDS"
echo "Data size:    ${N_MODELS} models × ${N_ITEMS} items"
echo ""

python3 "$SCRIPT_DIR/run_noise_propagation.py" \
    --stan-me "$STAN_ME" \
    --stan-simple "$STAN_SIMPLE" \
    --output-dir "$OUTPUT_DIR" \
    --n-seeds "$N_SEEDS" \
    --n-models "$N_MODELS" \
    --n-items "$N_ITEMS"

echo ""
echo "=== exp-005 complete ==="
echo "Results:  $OUTPUT_DIR/noise_propagation_results.json"
echo "Summary:  $OUTPUT_DIR/noise_propagation_summary.json"
