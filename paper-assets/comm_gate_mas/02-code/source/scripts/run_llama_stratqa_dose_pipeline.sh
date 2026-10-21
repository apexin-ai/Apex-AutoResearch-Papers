#!/bin/bash
set -euo pipefail
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/autodl-tmp/comm_gate_mas

# AutoDL network + HF cache
source /etc/network_turbo 2>/dev/null || true
export HF_HOME=/root/autodl-tmp/.hf_cache
export HF_DATASETS_OFFLINE=1
export HF_HUB_DISABLE_XET=1
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt

# Phase 1: Verify vLLM
echo "=== Phase 1: Verify vLLM ==="
for i in $(seq 1 30); do
    if curl -s --max-time 5 http://localhost:8001/v1/models > /dev/null 2>&1; then
        echo "vLLM ready"
        break
    fi
    echo "Waiting for vLLM... ($i/30)"
    sleep 10
done
if ! curl -s --max-time 5 http://localhost:8001/v1/models > /dev/null 2>&1; then
    echo "ABORT: vLLM not responding after 5 min"
    exit 1
fi

# Phase 2: Collect traces (100 tasks)
TRACES_DIR="outputs/stratqa/llama_round_robin/traces"
TRACES_FILE="$TRACES_DIR/traces.jsonl"
echo "=== Phase 2: Trace Collection ==="
if [[ -f "$TRACES_FILE" ]]; then
    NLINES=$(wc -l < "$TRACES_FILE")
    echo "Traces exist with $NLINES tasks, skipping collection"
else
    mkdir -p "$TRACES_DIR"
    python3 src/trace_collection.py \
        --config configs/stratqa_llama_rr.yaml \
        --num-tasks 100 \
        2>&1
    echo "Trace collection done"
fi

# Verify traces
if [[ ! -f "$TRACES_FILE" ]]; then
    echo "ABORT: traces.jsonl not created"
    exit 1
fi
NLINES=$(wc -l < "$TRACES_FILE")
echo "Traces: $NLINES tasks"

# Phase 3: Dose-response (5 rates x 5 seeds = 25 runs)
OUTPUT_DIR="outputs/analysis/dose_response_llama_stratqa"
mkdir -p "$OUTPUT_DIR"
echo "=== Phase 3: Dose-Response ==="

RATES=(0.0 0.25 0.50 0.75 1.0)
SEEDS=(42 123 456 789 1024)

for RATE in "${RATES[@]}"; do
    for SEED in "${SEEDS[@]}"; do
        OUTFILE="$OUTPUT_DIR/rate${RATE}_seed${SEED}.json"
        if [[ -f "$OUTFILE" ]]; then
            echo "[skip] rate=$RATE seed=$SEED exists"
            continue
        fi
        echo "=== rate=$RATE seed=$SEED ==="
        python3 src/dose_response.py \
            --config configs/dose_response_llama_stratqa.yaml \
            --ack-prune-rate "$RATE" \
            --subset-seed "$SEED" \
            --n-tasks 100 \
            --traces-dir "$TRACES_DIR" \
            --backbone llama \
            --output-dir "$OUTPUT_DIR" \
            2>&1
    done
done

# Phase 4: Summary
echo "=== Phase 4: Build Summary ==="
python3 src/dose_response.py \
    --config configs/dose_response_llama_stratqa.yaml \
    --summary-only \
    --output-dir "$OUTPUT_DIR" 2>&1 || echo "Summary build failed (non-fatal)"

echo "=== ALL DONE ==="
