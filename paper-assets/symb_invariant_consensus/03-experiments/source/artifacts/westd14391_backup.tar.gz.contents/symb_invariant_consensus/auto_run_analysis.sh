#!/bin/bash
LOG=/tmp/reextract_v3_log.txt
while true; do
    if grep -q "REEXTRACTION_COMPLETE" "$LOG" 2>/dev/null; then
        echo "$(date): Extraction done, running analysis..."
        cd /root/symb_invariant_consensus
        /root/miniconda3/bin/python3 run_ablation_analysis.py 2>&1
        echo "ANALYSIS_PIPELINE_DONE"
        break
    fi
    sleep 30
done
