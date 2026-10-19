#!/bin/bash
# v7.1 Probe A: cross-task cosine similarity check at step 5000
# Verifies language conditioning is active (cos < 0.8 = PASS)
#
# Usage: CUDA_VISIBLE_DEVICES=X bash run_v71_probe_a.sh <seed_dir> <step>
# Example: CUDA_VISIBLE_DEVICES=0 bash run_v71_probe_a.sh acib_v7.1_scorer_only_seed1 5000

SEED_DIR=${1:-acib_v7.1_scorer_only_seed1}
STEP=${2:-5000}
CKPT_DIR="/root/autodl-tmp/${SEED_DIR}"
OUT_DIR="/root/autodl-tmp/v71_probe/${SEED_DIR}_step${STEP}"

cd /root/acib
python3 -u scripts/cross_task_probe.py \
  --checkpoint_dir "${CKPT_DIR}" \
  --checkpoint_step "${STEP}" \
  --base_model lerobot/smolvla_libero \
  --gpu 0 \
  --out_dir "${OUT_DIR}"

echo ""
echo "=== PROBE RESULTS ==="
cat "${OUT_DIR}/probe_summary.json" 2>/dev/null || echo "No summary file found"
echo ""
echo "PASS criteria: all Probe A cosine similarities < 0.8"
