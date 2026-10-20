#!/bin/bash
# Monitor FOLIO seed=789 and chain PW experiments after completion
cd /root/symb_invariant_consensus

echo "Monitoring FOLIO seed=789 experiment (PID 10340)..."
while kill -0 10340 2>/dev/null; do
    DONE=$(grep -c "overall" /tmp/llama8b_folio_seed789.log 2>/dev/null || echo 0)
    echo "$(date '+%H:%M:%S') FOLIO progress: $DONE/204"
    sleep 60
done

echo "$(date) FOLIO seed=789 completed!"
echo ""

# Start PW experiments
echo "$(date) Starting PW multi-seed experiments..."
nohup bash scripts/run_after_folio.sh > /tmp/llama8b_pw_all.log 2>&1 &
echo "PW experiments PID: $!"
echo "SENTINEL_CHAIN_STARTED"
