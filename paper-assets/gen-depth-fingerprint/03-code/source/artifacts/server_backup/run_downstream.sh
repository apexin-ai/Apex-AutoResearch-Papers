#!/bin/bash
# Downstream utility experiments: fine-tune OLMo on depth-stratified data
# Usage: bash run_downstream.sh [GPU_ID]
# Runs all variants x 3 seeds, outputs to experiments/downstream/

set -e

GPU_ID=${1:-3}
MODEL_PATH="/root/autodl-tmp/models/olmo-2-1b-hf/allenai/OLMo-2-0425-1B"
DATA_DIR="data/downstream"
OUTPUT_BASE="experiments/downstream"
SEEDS="${2:-42 123 456}"

source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
export CUDA_VISIBLE_DEVICES=$GPU_ID

VARIANTS="${VARIANTS:-depth0_only depth01 all size_matched binary_filtered}"

echo "=== Downstream Utility Experiments ==="
echo "GPU: $GPU_ID  Model: $MODEL_PATH"
echo "Variants: $VARIANTS"
echo "Seeds: $SEEDS"
echo ""

for VARIANT in $VARIANTS; do
    TRAIN_FILE="$DATA_DIR/train_${VARIANT}.jsonl"
    if [ ! -f "$TRAIN_FILE" ]; then
        echo "SKIP: $TRAIN_FILE not found"
        continue
    fi

    for SEED in $SEEDS; do
        OUT_DIR="$OUTPUT_BASE/${VARIANT}_seed${SEED}"
        if [ -f "$OUT_DIR/results.json" ]; then
            echo "SKIP: $OUT_DIR/results.json already exists"
            continue
        fi

        echo ">>> variant=$VARIANT seed=$SEED"
        python3 finetune_downstream.py \
            --model-path "$MODEL_PATH" \
            --train-data "$TRAIN_FILE" \
            --eval-data "$DATA_DIR/test.jsonl" \
            --output-dir "$OUT_DIR" \
            --seed "$SEED" \
            --bf16 \
            --epochs 3 \
            --batch-size 4 \
            --grad-accum 4
        echo "<<< Done: $VARIANT seed=$SEED"
        echo ""
    done
done

echo ""
echo "=== Collecting Results ==="
python3 -c "
import json, os, glob
results = []
for p in sorted(glob.glob('$OUTPUT_BASE/*/results.json')):
    with open(p) as f:
        r = json.load(f)
    name = os.path.basename(os.path.dirname(p))
    results.append({'name': name, **r})
    print(f'{name}: ppl={r[\"eval_perplexity\"]:.2f}, loss={r[\"eval_loss\"]:.4f}')

with open('$OUTPUT_BASE/all_results.json', 'w') as f:
    json.dump(results, f, indent=2)
print(f'\nAll results saved to $OUTPUT_BASE/all_results.json')
"
