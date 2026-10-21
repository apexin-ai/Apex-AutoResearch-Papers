#!/bin/bash
set -euo pipefail

source /root/miniconda3/etc/profile.d/conda.sh
conda activate base

export HF_HOME=/root/autodl-tmp/.hf_cache
export HF_DATASETS_OFFLINE=1

cd /root/autodl-tmp/comm_gate_mas

THRESHOLDS=(150 200 250 300 350 400 500)
CONFIG="configs/llama_gsm8k_rr_temp07.yaml"
OUTDIR="outputs/heuristic_threshold_sweep_t07"
NUM_TASKS=100

mkdir -p "${OUTDIR}"

echo "=== Heuristic Threshold Sweep (t=0.7) ==="
echo "Thresholds: ${THRESHOLDS[*]}"
echo "Config: ${CONFIG}"
echo "Num tasks: ${NUM_TASKS}"
echo "Start time: $(date)"
echo ""

for T in "${THRESHOLDS[@]}"; do
    OUTFILE="${OUTDIR}/threshold_${T}.json"
    echo "--- Running threshold=${T} ---"
    echo "Output: ${OUTFILE}"
    echo "Start: $(date)"

    python3 src/pruning_validation.py \
        --mode online_pruning \
        --config "${CONFIG}" \
        --detection-mode length_only \
        --char-threshold "${T}" \
        --num-tasks "${NUM_TASKS}" \
        --output "${OUTFILE}" \
        2>&1

    echo "Finished threshold=${T} at $(date)"
    echo ""
done

echo "=== All thresholds complete at $(date) ==="

echo ""
echo "=== Summary ==="
for T in "${THRESHOLDS[@]}"; do
    OUTFILE="${OUTDIR}/threshold_${T}.json"
    if [ -f "${OUTFILE}" ]; then
        echo "threshold=${T}:"
        python3 -c "
import json
with open('${OUTFILE}') as f:
    d = json.load(f)
s = d.get('summary', d.get('results', {}))
print(f'  baseline_acc={s.get(\"baseline_accuracy\", \"N/A\")}')
print(f'  pruned_acc={s.get(\"pruned_accuracy\", s.get(\"ack_pruned_accuracy\", \"N/A\"))}')
print(f'  delta={s.get(\"delta\", s.get(\"accuracy_delta\", \"N/A\"))}')
print(f'  suppress_rate={s.get(\"suppress_rate\", s.get(\"ack_suppress_rate\", \"N/A\"))}')
"
    else
        echo "threshold=${T}: OUTPUT FILE MISSING"
    fi
done
