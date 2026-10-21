#!/bin/bash
# =============================================================================
# Reproduce Table 3: Layer Selection Sensitivity Results
# =============================================================================
# Table 3 shows how crossing-rate composite vs. threshold-based metrics
# select different layers, with downstream impact on HS vs. text conclusions.
# The layer sweep evaluates 5 metrics x 7 window sizes x L layers per model.
#
# Prerequisites:
#   - GPU: 1x RTX 4090 or equivalent (24GB VRAM)
#   - Pre-extracted hidden states for all 4 models
#   - Estimated runtime: ~1 hour per model (layer sweep + bootstrap)
#
# Environment variables:
#   DATA_DIR  — project root containing artifacts/
#   MODEL_DIR — directory containing downloaded model weights
# =============================================================================

set -euo pipefail

export DATA_DIR="${DATA_DIR:-.}"
export MODEL_DIR="${MODEL_DIR:-./models}"

echo "=== Step 1: Run layer sweep with bootstrap CI (R1-8B, AdvBench) ==="
python scripts/advbench_preliminary_sweep.py

echo ""
echo "=== Step 2: Threshold sensitivity analysis (32B models) ==="
python scripts/run_threshold_sensitivity.py

echo ""
echo "=== Step 3: Random CP control (QwQ-32B) ==="
echo "Verifies that shallow-layer bias is geometric, not CP-dependent."
python scripts/random_cp_control_qwq32b.py

echo ""
echo "Results will be saved to \$DATA_DIR/artifacts/ under respective experiment directories."
