#!/bin/bash
set -e
cd /root/projects/verifier-tts-struct-ie
PYTHON=/root/miniconda3/bin/python3
GOLD=data/test_gold.jsonl
OUTDIR=verify_results
MODEL=/root/autodl-tmp/models/Qwen/Qwen3-8B

mkdir -p $OUTDIR logs

echo "=== Starting verification ==="
echo "Time: $(date)"

for N in 4 8 16; do
    for SEED in 42 123 456; do
        echo ""
        echo "--- N=$N seed=$SEED ---"
        # Shards 0-3 on ports 8004-8007
        for SHARD in 0 1 2 3; do
            PORT=$((8004 + SHARD))
            FILE=results/test_shard_${SHARD}_n${N}_seed${SEED}.jsonl
            if [ -f "$FILE" ]; then
                $PYTHON scripts/verifier.py \
                    --results_file $FILE \
                    --gold_file $GOLD \
                    --port $PORT \
                    --model $MODEL \
                    --output_dir $OUTDIR \
                    --max_concurrent 16 &
            fi
        done
        wait

        # Shards 4-7 on ports 8004-8007
        for SHARD in 4 5 6 7; do
            PORT=$((8004 + SHARD - 4))
            FILE=results/test_shard_${SHARD}_n${N}_seed${SEED}.jsonl
            if [ -f "$FILE" ]; then
                $PYTHON scripts/verifier.py \
                    --results_file $FILE \
                    --gold_file $GOLD \
                    --port $PORT \
                    --model $MODEL \
                    --output_dir $OUTDIR \
                    --max_concurrent 16 &
            fi
        done
        wait
        echo "N=$N seed=$SEED done"
    done
done

echo ""
echo "=== All verification done ==="
echo "Time: $(date)"

# Run evaluation
echo ""
echo "=== Running evaluation ==="
$PYTHON scripts/verify_evaluate.py \
    --verify_dir $OUTDIR \
    --results_dir results \
    --gold_file $GOLD \
    --output_file $OUTDIR/verify_final_results.json

echo ""
echo "=== Complete ==="
