#!/usr/bin/env bash
set -euo pipefail

cd /root/gen-depth-fingerprint
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

GEN_PID=194539
GEN_FILE="data/generations/qwen3-14b-base/generations_shard0.jsonl"
MIN_LINES=2400

echo "$(date '+%F %T') [exp060] Pipeline started. Waiting for PID $GEN_PID ..."

# --- Phase 1: Wait for generation to finish ---
while kill -0 "$GEN_PID" 2>/dev/null; do
    LINES=$(wc -l < "$GEN_FILE" 2>/dev/null || echo 0)
    echo "$(date '+%F %T') [wait] PID $GEN_PID alive, $GEN_FILE has $LINES lines"
    sleep 60
done

LINES=$(wc -l < "$GEN_FILE" 2>/dev/null || echo 0)
echo "$(date '+%F %T') [wait] PID $GEN_PID exited. $GEN_FILE has $LINES lines."

if [ "$LINES" -lt "$MIN_LINES" ]; then
    echo "$(date '+%F %T') [ERROR] Only $LINES lines (need >= $MIN_LINES). Aborting."
    exit 1
fi
echo "$(date '+%F %T') [wait] Line count OK ($LINES >= $MIN_LINES). Proceeding."

# --- Phase 2: Feature extraction ---
echo "$(date '+%F %T') [extract] Starting feature extraction ..."
python3 extract_features.py \
    --input "$GEN_FILE" \
    --output data/features_qwen3-14b-base.csv \
    --device cuda:0 \
    --batch-size 8

echo "$(date '+%F %T') [extract] Feature extraction done."
wc -l data/features_qwen3-14b-base.csv

# --- Phase 3: DDR analysis ---
echo "$(date '+%F %T') [ddr] Starting DDR analysis ..."
python3 scripts/exp060_ddr_analysis.py

echo "$(date '+%F %T') [ddr] DDR analysis done."
echo "$(date '+%F %T') [exp060] Pipeline complete."
