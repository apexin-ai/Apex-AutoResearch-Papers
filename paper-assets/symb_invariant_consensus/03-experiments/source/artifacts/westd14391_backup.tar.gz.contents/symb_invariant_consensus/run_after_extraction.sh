#!/bin/bash
echo "Waiting for extraction to complete..."
while ! grep -q "EXTRACTION_COMPLETE" /tmp/extraction_v4.log 2>/dev/null; do
    sleep 30
    good=$(/root/miniconda3/bin/python3 -c "
import os, json
d = '/root/symb_invariant_consensus/results/folio_204_14b/per_trace_constraints'
print(sum(1 for fn in os.listdir(d) if any(len(t.get('constraints',[])) > 0 for t in json.load(open(os.path.join(d, fn))).get('per_trace',[]))))
" 2>/dev/null)
    echo "$(date '+%H:%M:%S') Extraction progress: $good/204"
done
echo "Extraction complete! Running analysis..."
cd /root/symb_invariant_consensus
/root/miniconda3/bin/python3 run_ablation_analysis.py 2>&1
echo "ALL_DONE"
