#!/bin/bash
# MVP 1.3B evaluation
# Usage: bash run_mvp_1.3b.sh [model_path1] [model_path2] ...
# If no args, runs all 16 models (skips those not yet downloaded)

set -e
source ${CONDA_SH:-$HOME/miniconda3/etc/profile.d/conda.sh} && conda activate base
export PATH=/usr/local/cuda/bin:$PATH
cd ${PROJECT_ROOT:-.}

MODELS_DIR="${MODEL_DIR:-./models_1.3b}"
BATCH_SIZE=${BATCH_SIZE:-32}
NUM_SAMPLES=${NUM_SAMPLES:-500}
NUM_SHOTS=6
DEVICE=${DEVICE:-cuda:0}

if [ $# -gt 0 ]; then
    MODELS=("$@")
else
    MODELS=(
        "$MODELS_DIR/transformer_1.3B_baseline"
        "$MODELS_DIR/1.3B-100B-GatedDeltaNet-hybrid-24-1"
        "$MODELS_DIR/1.3B-100B-GatedDeltaNet-hybrid-12-1"
        "$MODELS_DIR/1.3B-100B-GatedDeltaNet-hybrid-6-1"
        "$MODELS_DIR/1.3B-100B-GatedDeltaNet-hybrid-3-1"
        "$MODELS_DIR/1.3B-100B-GatedDeltaNet-pure"
        "$MODELS_DIR/1.3B-100B-HGRN2-hybrid-24-1"
        "$MODELS_DIR/1.3B-100B-HGRN2-hybrid-12-1"
        "$MODELS_DIR/1.3B-100B-HGRN2-hybrid-6-1"
        "$MODELS_DIR/1.3B-100B-HGRN2-hybrid-3-1"
        "$MODELS_DIR/1.3B-100B-HGRN2-pure"
        "$MODELS_DIR/1.3B-100B-RetNet-hybrid-24-1"
        "$MODELS_DIR/1.3B-100B-RetNet-hybrid-12-1"
        "$MODELS_DIR/1.3B-100B-RetNet-hybrid-6-1"
        "$MODELS_DIR/1.3B-100B-RetNet-hybrid-3-1"
        "$MODELS_DIR/1.3B-100B-RetNet-pure"
    )
fi

READY_MODELS=()
for m in "${MODELS[@]}"; do
    name=$(basename "$m")
    if [ -f "$m/config.json" ] && (ls "$m"/*.safetensors 1>/dev/null 2>&1); then
        min_size=$(stat -c%s "$m"/*.safetensors 2>/dev/null | sort -n | head -1)
        if [ "$min_size" -gt 100000000 ]; then
            READY_MODELS+=("$m")
            echo "READY: $name"
        else
            echo "SKIP (incomplete download): $name (smallest shard: ${min_size} bytes)"
        fi
    else
        echo "SKIP (not ready): $name"
    fi
done

if [ ${#READY_MODELS[@]} -eq 0 ]; then
    echo "ERROR: No models ready. Check download progress."
    exit 1
fi

echo ""
echo "=== Running with ${#READY_MODELS[@]} models, batch_size=$BATCH_SIZE, samples=$NUM_SAMPLES ==="
echo ""

echo "=== Generation evaluation ==="
python3 scripts/eval_composition.py \
    --models "${READY_MODELS[@]}" \
    --depths 1 2 3 4 5 \
    --num-samples $NUM_SAMPLES \
    --num-shots $NUM_SHOTS \
    --batch-size $BATCH_SIZE \
    --output-dir results/1.3b_mvp_gen \
    --variant direct \
    --device $DEVICE

echo ""
echo "=== Logprob evaluation ==="
python3 scripts/eval_logprob.py \
    --models "${READY_MODELS[@]}" \
    --depths 1 2 3 4 5 \
    --num-samples $NUM_SAMPLES \
    --num-shots $NUM_SHOTS \
    --batch-size $BATCH_SIZE \
    --output-dir results/1.3b_mvp_logprob \
    --variant direct \
    --device $DEVICE

echo ""
echo "=== DONE ==="
echo "Generation results: results/1.3b_mvp_gen/"
echo "Logprob results:    results/1.3b_mvp_logprob/"
