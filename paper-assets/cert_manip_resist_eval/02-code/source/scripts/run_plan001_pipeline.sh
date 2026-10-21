#!/bin/bash
set -e
cd /root/cert_manip_resist_eval

source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

echo "============================================"
echo "Plan 001 Pipeline: Steps 3 → Confound → 4 → 5"
echo "============================================"

echo ""
echo "=== Step 3: MI Matrix ==="
python scripts/run_plan001_step3_mi_matrix.py

echo ""
echo "=== Confound Diagnosis ==="
python scripts/run_plan001_confound_diagnosis.py

echo ""
echo "=== Step 4: Panel Regression ==="
python scripts/run_plan001_step4_panel_regression.py

echo ""
echo "=== Step 5: Random Fault ==="
python scripts/run_plan001_step5_random_fault.py

echo ""
echo "============================================"
echo "ALL DONE"
echo "============================================"
