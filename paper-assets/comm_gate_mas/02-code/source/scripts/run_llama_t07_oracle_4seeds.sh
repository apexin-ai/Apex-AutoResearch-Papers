#!/bin/bash
# Llama×GSM8K t=0.7 oracle pruning: 4 remaining seeds (vLLM managed externally)
set -euo pipefail

source /root/miniconda3/etc/profile.d/conda.sh
eval "$(grep '^export OPENAI_API_KEY' /root/.bashrc)"
eval "$(grep '^export ORACLE_BASE_URL' /root/.bashrc)"
conda activate base
cd /root/autodl-tmp/comm_gate_mas

export CUDA_VISIBLE_DEVICES=0
export HF_DATASETS_OFFLINE=1
export HF_HUB_OFFLINE=1
export HF_HOME=/root/autodl-tmp/.hf_cache
: "${OPENAI_API_KEY:[REDACTED] not set}"

CONFIG="configs/oracle_llama_gsm8k_t07_5seed.yaml"
OUTDIR="outputs/llama_oracle_t07_gsm8k"
VLLM_PORT=8001
SEEDS=(123 456 789 1024)
NUM_TASKS=200

echo "=== Llama t=0.7 oracle 4-seed rerun (N=$NUM_TASKS) starting at $(date) ==="

# Verify vLLM is alive
if ! curl -s --max-time 5 http://localhost:$VLLM_PORT/v1/models > /dev/null 2>&1; then
    echo "FATAL: vLLM not reachable on port $VLLM_PORT. Start it first."
    exit 1
fi
echo "vLLM confirmed alive on port $VLLM_PORT"

FAILED=0
for seed in "${SEEDS[@]}"; do
    echo ""
    echo "--- Seed $seed starting at $(date) ---"

    # Pre-check vLLM still alive
    if ! curl -s --max-time 5 http://localhost:$VLLM_PORT/v1/models > /dev/null 2>&1; then
        echo "ERROR: vLLM died before seed $seed. Aborting."
        exit 1
    fi

    python src/pruning_validation.py \
        --mode online_oracle \
        --config "$CONFIG" \
        --num-tasks $NUM_TASKS \
        --data-seed "$seed" \
        --detection-mode oracle_5class \
        --output "${OUTDIR}/seed_${seed}.json" \
        2>&1 | tee "${OUTDIR}/seed_${seed}.log"

    EXIT_CODE=${PIPESTATUS[0]}
    if [ $EXIT_CODE -ne 0 ]; then
        echo "WARNING: Seed $seed failed with exit code $EXIT_CODE"
        FAILED=$((FAILED + 1))
        continue
    fi

    if [ -f "${OUTDIR}/seed_${seed}.json" ]; then
        python3 -c "
import json
d = json.load(open('${OUTDIR}/seed_${seed}.json'))
bl = d.get('baseline', {})
op = d.get('oracle_pruned', {})
print(f'  Seed $seed: baseline={bl.get(\"accuracy\",0):.1%} oracle={op.get(\"accuracy\",0):.1%} delta={d.get(\"delta_pp\",0):+.1f}pp suppress={op.get(\"suppression_rate\",0):.1f}%')
" 2>/dev/null || echo "  (could not parse result)"
    fi

    echo "--- Seed $seed done at $(date) ---"
done

if [ $FAILED -gt 0 ]; then
    echo ""
    echo "WARNING: $FAILED seed(s) failed"
fi

echo ""
echo "=== ALL 4 SEEDS DONE at $(date) ==="
