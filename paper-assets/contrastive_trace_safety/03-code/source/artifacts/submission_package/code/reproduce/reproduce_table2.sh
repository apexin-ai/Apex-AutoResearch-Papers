#!/bin/bash
# =============================================================================
# Reproduce Table 2: HS vs. Text Comparison (main results)
# =============================================================================
# Table 2 reports HS vs. text precision differences at threshold-based layers
# for 4 models (R1-8B, OT-7B, QwQ-32B, R1-32B) against MiniLM-384d and
# BGE-large-1024d text encoders, with 10,000 bootstrap resamples and
# Holm-Bonferroni correction.
#
# Prerequisites:
#   - GPU: 1x RTX 4090 or equivalent (24GB VRAM for 8B models; 2x for 32B)
#   - Pre-extracted hidden states in $DATA_DIR/artifacts/hidden_states*/
#   - Pre-extracted text embeddings
#   - Estimated runtime: ~30 min per model (bootstrap), ~2 hours total
#
# Environment variables:
#   DATA_DIR  — project root containing artifacts/
#   MODEL_DIR — directory containing downloaded model weights
# =============================================================================

set -euo pipefail

export DATA_DIR="${DATA_DIR:-.}"
export MODEL_DIR="${MODEL_DIR:-./models}"

echo "=== Step 1: Extract hidden states (if not already done) ==="
echo "For R1-8B (layers 12-24):"
python -m src.run_pipeline --step extract

echo ""
echo "=== Step 2: Run bootstrap CI for HS vs. text comparison ==="
echo "This runs 10,000 bootstrap resamples for each model."
python -m src.experiments.bootstrap_ci

echo ""
echo "=== Step 3: Run FPR analysis ==="
python -m src.experiments.fpr_analysis

echo ""
echo "Results will be saved to \$DATA_DIR/artifacts/exp_006_bootstrap/"
echo "and \$DATA_DIR/artifacts/exp_015_fpr/"
