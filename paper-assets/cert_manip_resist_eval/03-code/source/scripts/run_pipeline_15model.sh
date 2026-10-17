#!/bin/bash
# 15-model pipeline: Step 3 -> Confound -> Step 4 -> Step 5
# Prereq: individual_scores/ has all 9 API model x 14 condition JSON files
set -e
cd /root/cert_manip_resist_eval
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

echo "=== Step 3: MI Matrix (105 pairs, 455 panels) ==="
python scripts/run_plan001_step3_mi_matrix.py

echo ""
echo "=== Confound Diagnosis ==="
python scripts/run_plan001_confound_diagnosis.py

echo ""
echo "=== Step 4: Panel Regression (455 panels x 12 conditions) ==="
python scripts/run_plan001_step4_panel_regression.py

echo ""
echo "=== Step 5: Random-Fault Simulation (455 panels x 1000 sims) ==="
python scripts/run_plan001_step5_random_fault.py

echo ""
echo "=== PIPELINE COMPLETE ==="
echo "Results in: /root/cert_manip_resist_eval/artifacts/results/plan001/"
ls -la /root/cert_manip_resist_eval/artifacts/results/plan001/mi_matrix/ 2>/dev/null
ls -la /root/cert_manip_resist_eval/artifacts/results/plan001/panel_regression/ 2>/dev/null
ls -la /root/cert_manip_resist_eval/artifacts/results/plan001/confound_*.{json,png} 2>/dev/null
