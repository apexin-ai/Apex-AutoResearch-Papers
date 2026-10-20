#!/bin/bash
# Wait for old process to finish, then rerun with fixed code
source /root/miniconda3/etc/profile.d/conda.sh
conda activate base

echo "Waiting for PID 223500 to finish..."
while kill -0 223500 2>/dev/null; do
    sleep 30
done
echo "PID 223500 finished at $(date)"

# Save old results if they exist
if [ -f /root/gen-depth-fingerprint/results/human_edit_robustness.json ]; then
    cp /root/gen-depth-fingerprint/results/human_edit_robustness.json \
       /root/gen-depth-fingerprint/results/human_edit_robustness_old_no_chat_template.json
    echo "Old results saved"
fi

echo "Starting rerun with chat template fix at $(date)"
cd /root/gen-depth-fingerprint
python3 experiments/human_edit_robustness.py --device cuda:1 --rephrase-batch-size 16
echo "Rerun completed at $(date)"
