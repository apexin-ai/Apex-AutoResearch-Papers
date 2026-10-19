#!/bin/bash
# =============================================================================
# Reproduce Table 4: Three-Layer Ensemble Results
# =============================================================================
# Table 4 shows that a three-layer ensemble (precision-best, BA-best,
# FPR-best layers) provides metric-agnostic HS advantage across all 4 models
# (p <= 0.002), matching or exceeding the best individual metric.
#
# Prerequisites:
#   - GPU: 1x RTX 4090 or equivalent (24GB VRAM for 8B; 2x for 32B)
#   - Pre-extracted hidden states for all 4 models
#   - Estimated runtime: ~2 hours total (10,000 bootstrap resamples per model)
#
# Environment variables:
#   DATA_DIR  — project root containing artifacts/
#   MODEL_DIR — directory containing downloaded model weights
# =============================================================================

set -euo pipefail

export DATA_DIR="${DATA_DIR:-.}"
export MODEL_DIR="${MODEL_DIR:-./models}"

echo "=== Running N6 Multi-Metric Layer Ensemble ==="
echo "Models: R1-8B, OT-7B, QwQ-32B, R1-32B"
echo "For each model: trains probes at 3 candidate layers, ensembles predictions,"
echo "then runs 10,000 bootstrap resamples for ensemble vs. text and ensemble vs. best-single."
echo ""

python scripts/n6_multi_metric_ensemble.py

echo ""
echo "Results will be saved to \$DATA_DIR/artifacts/n6_multi_metric_ensemble/"
