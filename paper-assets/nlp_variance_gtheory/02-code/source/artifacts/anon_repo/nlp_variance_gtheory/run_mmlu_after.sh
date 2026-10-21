#!/bin/bash
source $CONDA_PREFIX/etc/profile.d/conda.sh
conda activate base
echo "$(date): Waiting for PID 334256 to finish..."
while kill -0 334256 2>/dev/null; do sleep 60; done
echo "$(date): Main inference done, starting MMLU rerun..."
cd .
python scripts/exp_llama70b/run_llama70b_inference.py
echo "$(date): MMLU rerun complete"
