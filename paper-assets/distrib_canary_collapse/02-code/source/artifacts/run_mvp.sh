#!/usr/bin/env bash
# Run MVP experiment: 3 repetitions with different seeds.
# Each rep runs iterative_train.py with 100% synthetic ratio for 10 generations.
#
# Usage:
#   bash run_mvp.sh                    # default settings
#   bash run_mvp.sh --steps_per_gen 5000  # override any iterative_train.py arg

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SEEDS=(42 43 44)
DATA_DIR="${DATA_DIR:-data/wikitext103}"
RESULTS_DIR="${RESULTS_DIR:-results/mvp}"

# Step 1: Prepare data (idempotent — skips if already exists)
if [ ! -d "$DATA_DIR/train" ]; then
    echo "=== Preparing data ==="
    python "$SCRIPT_DIR/prepare_data.py" --output_dir "$DATA_DIR"
fi

# Step 2: Run each repetition
for SEED in "${SEEDS[@]}"; do
    OUTPUT="$RESULTS_DIR/rep_${SEED}"

    if [ -f "$OUTPUT/all_metrics.json" ]; then
        echo "=== Seed $SEED already completed, skipping ==="
        continue
    fi

    echo "=== Running seed=$SEED ==="
    python "$SCRIPT_DIR/iterative_train.py" \
        --data_dir "$DATA_DIR" \
        --output_dir "$OUTPUT" \
        --seed "$SEED" \
        --synthetic_ratio 1.0 \
        --num_generations 10 \
        --steps_per_gen 5000 \
        "$@"

    echo "=== Seed $SEED complete ==="
done

# Step 3: Analyze results
echo "=== Analyzing results ==="
python "$SCRIPT_DIR/analyze_mvp.py" \
    --results_dir "$RESULTS_DIR" \
    --seeds 42 43 44

echo "=== MVP experiment complete ==="
