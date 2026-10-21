#!/bin/bash
# P2 v5: Oracle online pruning via OpenRouter → GPT-4o-mini (D213/D215)
# All oracle labels via API (no cache — D215: avoid GPT-4o/GPT-4o-mini label mixing)
# .env.p2 provides OPENAI_API_KEY, ORACLE_BASE_URL, ORACLE_MODEL
#
# Prerequisites:
#   1. vLLM server running on localhost:8001 (Llama-3.1-8B-Instruct)
#   2. .env.p2 with OpenRouter credentials
set -euo pipefail

# AutoDL network proxy for external API access (GPT-4o oracle)
if [ -f /etc/network_turbo ]; then
    source /etc/network_turbo
fi

source /root/miniconda3/etc/profile.d/conda.sh
conda activate base

cd /root/autodl-tmp/comm_gate_mas

# Load API keys from temporary env file
if [ -f .env.p2 ]; then
    source .env.p2
fi

export CUDA_VISIBLE_DEVICES=1

CONFIG="configs/oracle_online_llama_gsm8k.yaml"
OUTDIR="outputs/oracle_online_llama_v5"

# --- Pre-flight checks ---

if [ -z "${OPENAI_API_KEY:[REDACTED]}" ]; then
    echo "ERROR: OPENAI_API_KEY not set"
    exit 1
fi

if ! curl -s --max-time 5 http://localhost:8001/v1/models > /dev/null 2>&1; then
    echo "ERROR: vLLM server not responding on localhost:8001"
    exit 1
fi

# Verify model name matches vLLM served model
SERVED_MODEL=$(curl -s http://localhost:8001/v1/models | python3 -c "import sys,json; print(json.load(sys.stdin)['data'][0]['id'])" 2>/dev/null)
CONFIG_MODEL=$(python3 -c "import yaml; print(yaml.safe_load(open('$CONFIG'))['model']['name'])" 2>/dev/null)
if [ "$SERVED_MODEL" != "$CONFIG_MODEL" ]; then
    echo "ERROR: Model name mismatch — vLLM serves '$SERVED_MODEL' but config has '$CONFIG_MODEL'"
    exit 1
fi
echo "Model name verified: $SERVED_MODEL"

# D215: No oracle cache — all labels via GPT-4o-mini API to avoid label mixing
echo "Oracle mode: all labels via API (ORACLE_MODEL=${ORACLE_MODEL:-gpt-4o})"

mkdir -p "$OUTDIR"

echo "=== P2 oracle_online starting at $(date) ==="

for seed in 42 123 456; do
    echo "--- Seed $seed at $(date) ---"
    python src/pruning_validation.py \
        --mode online_oracle \
        --config "$CONFIG" \
        --num-tasks 200 \
        --data-seed "$seed" \
        --detection-mode oracle_5class \
        --output "${OUTDIR}/seed_${seed}.json" \
        2>&1

    echo "--- Seed $seed done (exit=$?) at $(date) ---"

    # Fail-fast: check skip ratio in output
    if [ -f "${OUTDIR}/seed_${seed}.json" ]; then
        SKIP_PCT=$(python3 -c "
import json
d = json.load(open('${OUTDIR}/seed_${seed}.json'))
total = d.get('online_pruned',{}).get('total',0) or d.get('baseline',{}).get('total',0) or 200
skipped = d.get('online_pruned',{}).get('skipped',0) + d.get('baseline',{}).get('skipped',0)
print(int(100*skipped/max(total,1)))
" 2>/dev/null || echo "0")
        if [ "$SKIP_PCT" -gt 50 ] 2>/dev/null; then
            echo "ABORT: seed $seed has ${SKIP_PCT}% skipped tasks — likely infrastructure error"
            exit 1
        fi
    fi
done

echo "=== P2 ALL SEEDS COMPLETE at $(date) ==="
