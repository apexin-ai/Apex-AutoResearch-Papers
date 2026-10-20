#!/bin/bash
set -eo pipefail

SCRIPT_DIR="/root/occsafe_vla/scripts"
ANALYSIS_SCRIPT="${SCRIPT_DIR}/same_seed_gradient_analysis.py"
PLOT_SCRIPT="${SCRIPT_DIR}/plot_gradient_comparison.py"
OUTPUT_DIR="/root/autodl-tmp/analysis/gradient_same_seed"
LOG_FILE="${OUTPUT_DIR}/run.log"

CKPT_SUBDIR="openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt"
CKPT_BASE="/root/autodl-tmp/checkpoints"

mkdir -p "${OUTPUT_DIR}"

source /root/miniconda3/etc/profile.d/conda.sh
conda activate occsafe

export CUDA_VISIBLE_DEVICES=0

echo "=== Same-Seed Gradient Analysis (4 conditions) ===" | tee "${LOG_FILE}"
echo "Start: $(date)" | tee -a "${LOG_FILE}"

# Condition 1: Vanilla
echo "" | tee -a "${LOG_FILE}"
echo ">>> [1/4] Vanilla (seed=42)" | tee -a "${LOG_FILE}"
python "${ANALYSIS_SCRIPT}" \
    --checkpoint_path "${CKPT_BASE}/vanilla_retrain_s0/${CKPT_SUBDIR}" \
    --condition_name vanilla \
    --occ_detach true \
    --occ_norm bn \
    --output_dir "${OUTPUT_DIR}" \
    --gpu 0 --seed 42 --num_batches 200 --batch_size 4 \
    2>&1 | tee -a "${LOG_FILE}"

# Condition 2: Full OCC + BN
echo "" | tee -a "${LOG_FILE}"
echo ">>> [2/4] Full OCC + BN (seed=42)" | tee -a "${LOG_FILE}"
python "${ANALYSIS_SCRIPT}" \
    --checkpoint_path "${CKPT_BASE}/full_occ_retrain_s0/${CKPT_SUBDIR}" \
    --condition_name full_occ_bn \
    --occ_detach false \
    --occ_norm bn \
    --output_dir "${OUTPUT_DIR}" \
    --gpu 0 --seed 42 --num_batches 200 --batch_size 4 \
    2>&1 | tee -a "${LOG_FILE}"

# Condition 3: Detach + BN
echo "" | tee -a "${LOG_FILE}"
echo ">>> [3/4] Detach + BN (seed=42)" | tee -a "${LOG_FILE}"
python "${ANALYSIS_SCRIPT}" \
    --checkpoint_path "${CKPT_BASE}/ablation_occ_detach_s0_retrain/${CKPT_SUBDIR}" \
    --condition_name detach_bn \
    --occ_detach true \
    --occ_norm bn \
    --output_dir "${OUTPUT_DIR}" \
    --gpu 0 --seed 42 --num_batches 200 --batch_size 4 \
    2>&1 | tee -a "${LOG_FILE}"

# Condition 4: Full OCC + LN
echo "" | tee -a "${LOG_FILE}"
echo ">>> [4/4] Full OCC + LN (seed=42)" | tee -a "${LOG_FILE}"
python "${ANALYSIS_SCRIPT}" \
    --checkpoint_path "${CKPT_BASE}/full_occ_ln_s0/${CKPT_SUBDIR}" \
    --condition_name full_occ_ln \
    --occ_detach false \
    --occ_norm ln \
    --output_dir "${OUTPUT_DIR}" \
    --gpu 0 --seed 42 --num_batches 200 --batch_size 4 \
    2>&1 | tee -a "${LOG_FILE}"

# Combine JSONs into gradient_results.json
echo "" | tee -a "${LOG_FILE}"
echo ">>> Combining results..." | tee -a "${LOG_FILE}"
python -c "
import json, glob, os
results = {}
for f in sorted(glob.glob('${OUTPUT_DIR}/*_gradient_stats.json')):
    with open(f) as fh:
        data = json.load(fh)
    results[data['condition']] = data
    print(f'  Loaded: {os.path.basename(f)} -> {data[\"condition\"]}')
out = '${OUTPUT_DIR}/gradient_results.json'
with open(out, 'w') as fh:
    json.dump(results, fh, indent=2)
print(f'Combined {len(results)} conditions -> {out}')
" 2>&1 | tee -a "${LOG_FILE}"

# Generate plots
echo "" | tee -a "${LOG_FILE}"
echo ">>> Generating plots..." | tee -a "${LOG_FILE}"
python "${PLOT_SCRIPT}" \
    --results_dir "${OUTPUT_DIR}" \
    --output_dir "${OUTPUT_DIR}" \
    2>&1 | tee -a "${LOG_FILE}"

# Copy summary to expected name
if [ -f "${OUTPUT_DIR}/gradient_summary.pdf" ]; then
    cp "${OUTPUT_DIR}/gradient_summary.pdf" "${OUTPUT_DIR}/gradient_analysis.pdf"
    echo "Copied gradient_summary.pdf -> gradient_analysis.pdf" | tee -a "${LOG_FILE}"
fi

echo "" | tee -a "${LOG_FILE}"
echo "=== DONE ===" | tee -a "${LOG_FILE}"
echo "End: $(date)" | tee -a "${LOG_FILE}"
echo "Results: ${OUTPUT_DIR}/gradient_results.json" | tee -a "${LOG_FILE}"
echo "Figures: ${OUTPUT_DIR}/gradient_analysis.pdf" | tee -a "${LOG_FILE}"
