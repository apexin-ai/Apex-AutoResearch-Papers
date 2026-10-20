#!/usr/bin/env bash
# exp-003: RRF Ablation — evaluate aggregation variants against ground truth
#
# Usage:
#   bash run_exp003.sh
#   SIGNAL_DIR=/path/to/signals LABELS_DIR=/path/to/labels bash run_exp003.sh

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
DATA_DIR="${DATA_DIR:-/root/contamcal-irt-calibration/data}"
SIGNAL_DIR="${SIGNAL_DIR:-${DATA_DIR}/signals}"
LABELS_DIR="${LABELS_DIR:-${DATA_DIR}/labels}"
OUTPUT_DIR="${OUTPUT_DIR:-/root/contamcal-irt-calibration/results/exp003}"
BENCHMARKS="${BENCHMARKS:-mmlu gsm8k arc_challenge humaneval}"
DOSAGE="${DOSAGE:-}"

mkdir -p "$OUTPUT_DIR"

echo "=== exp-003: RRF Ablation Analysis ==="
echo "Signal dir:  $SIGNAL_DIR"
echo "Labels dir:  $LABELS_DIR"
echo "Output dir:  $OUTPUT_DIR"
echo "Benchmarks:  $BENCHMARKS"
echo ""

DOSAGE_FLAG=""
if [[ -n "$DOSAGE" ]]; then
    DOSAGE_FLAG="--dosage $DOSAGE"
fi

python3 "$SCRIPT_DIR/analyze_rrf_ablation.py" \
    --signal-dir "$SIGNAL_DIR" \
    --labels-dir "$LABELS_DIR" \
    --output-dir "$OUTPUT_DIR" \
    --benchmarks $BENCHMARKS \
    $DOSAGE_FLAG

echo ""
echo "=== exp-003 complete ==="
echo "Results: $OUTPUT_DIR/rrf_ablation_results.json"
echo "Table:   $OUTPUT_DIR/rrf_ablation_table.tex"
