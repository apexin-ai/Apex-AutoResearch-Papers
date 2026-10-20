#!/bin/bash
# T=20 batch verify: run 5-method analysis + prediction check for all completed experiments
set -euo pipefail

PROJ="/root/autodl-tmp/distrib_canary_collapse"
PRED="$PROJ/artifacts/t20_predictions_locked.json"
RESULTS_DIR="$PROJ/results/t20"
OUT_DIR="$PROJ/artifacts"

ALPHAS=("0.45" "0.50" "0.60" "0.75" "1.00")
SEED=42
EXPECTED_GENS=21  # gen_0..gen_20

passed=0
failed=0
skipped=0

echo "============================================================"
echo "T=20 BATCH VERIFICATION"
echo "Predictions: $PRED"
echo "Results dir: $RESULTS_DIR"
echo "============================================================"

for alpha in "${ALPHAS[@]}"; do
    alpha_tag=$(echo "$alpha" | tr -d '.')
    exp_dir="$RESULTS_DIR/a${alpha_tag}_s${SEED}_fp32"

    echo ""
    echo "--- alpha=$alpha  dir=$exp_dir ---"

    if [ ! -d "$exp_dir" ]; then
        echo "  SKIP: directory not found"
        ((skipped++))
        continue
    fi

    # Check completeness: last gen must have metrics.json
    last_gen=$((EXPECTED_GENS - 1))
    if [ ! -f "$exp_dir/gen_${last_gen}/metrics.json" ]; then
        echo "  SKIP: gen_${last_gen}/metrics.json not found (experiment incomplete)"
        ((skipped++))
        continue
    fi

    python3 "$PROJ/scripts/t20_post_analysis.py" \
        --exp_dir "$exp_dir" \
        --alpha "$alpha" \
        --seed "$SEED" \
        --predictions "$PRED" \
        --output_dir "$OUT_DIR"

    # Check result
    verify_file="$OUT_DIR/t20_verify_a${alpha_tag}_s${SEED}.json"
    if [ -f "$verify_file" ]; then
        within_ci=$(python3 -c "import json; print(json.load(open('$verify_file'))['within_ci'])")
        if [ "$within_ci" = "True" ]; then
            echo "  => PASS (within 95% CI)"
            ((passed++))
        else
            echo "  => FAIL (outside 95% CI)"
            ((failed++))
        fi
    fi
done

echo ""
echo "============================================================"
echo "SUMMARY: $passed passed, $failed failed, $skipped skipped (of ${#ALPHAS[@]} total)"
echo "============================================================"
