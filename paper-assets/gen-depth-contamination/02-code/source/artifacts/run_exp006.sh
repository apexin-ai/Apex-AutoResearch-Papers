#!/bin/bash
# exp006 orchestrator — run all strategy x seed combinations (train + eval).
#
# Usage:
#   bash run_exp006.sh --strategy all --seeds "42 123 456 789 1024"
#   bash run_exp006.sh --strategy graduated --alpha "0.1 0.3 0.5 0.7 0.9"
#   bash run_exp006.sh --strategy binary-ours --seeds "42"
set -euo pipefail

PROJECT_DIR="/root/autodl-tmp/gen-depth-contamination"
OUTPUT_BASE="${PROJECT_DIR}/outputs/exp006"
SCRIPTS_DIR="${PROJECT_DIR}/scripts"
DATA_DIR="${PROJECT_DIR}/data"
MODEL="Qwen/Qwen2.5-1.5B-Instruct"
CACHE_DIR="/root/autodl-tmp/.hf_cache"

ALL_STRATEGIES="no-filter binary-ours binary-drayson graduated surprisal dsir"
STRATEGIES="$ALL_STRATEGIES"
SEEDS="42 123 456 789 1024"
ALPHAS="0.1 0.3 0.5 0.7 0.9"

while [[ $# -gt 0 ]]; do
    case $1 in
        --strategy)
            if [ "$2" = "all" ]; then STRATEGIES="$ALL_STRATEGIES"; else STRATEGIES="$2"; fi
            shift 2 ;;
        --seeds)  SEEDS="$2";  shift 2 ;;
        --alpha)  ALPHAS="$2"; shift 2 ;;
        *) echo "Unknown: $1"; exit 1 ;;
    esac
done

source /root/miniconda3/etc/profile.d/conda.sh
conda activate base

mkdir -p "$OUTPUT_BASE"

# Count runs
total_runs=0
for s in $STRATEGIES; do
    for seed in $SEEDS; do
        if [ "$s" = "graduated" ]; then
            for _ in $ALPHAS; do total_runs=$((total_runs + 1)); done
        else
            total_runs=$((total_runs + 1))
        fi
    done
done

# ~25 min per run (15 min train + 10 min eval on 4090 with 1.5B LoRA)
est_hours=$(echo "scale=1; $total_runs * 25 / 60" | bc)
echo "=== exp006 Graduated Filtering Evaluation ==="
echo "Strategies: $STRATEGIES"
echo "Seeds:      $SEEDS"
echo "Alphas:     $ALPHAS (graduated only)"
echo "Total runs: $total_runs"
echo "Est. GPU time: ~${est_hours}h (~${total_runs}x25min)"
echo ""

run_one() {
    local strategy=$1 seed=$2 alpha=$3 tag=$4
    local out_dir="${OUTPUT_BASE}/${tag}"
    local result_file="${out_dir}/eval_results.json"

    if [ -f "$result_file" ]; then
        echo "  SKIP (results exist)"
        return 0
    fi

    local extra_args=""
    if [ "$strategy" = "graduated" ]; then
        extra_args="--alpha $alpha"
    fi

    echo "  Training..."
    python3 "${SCRIPTS_DIR}/exp006_continued_pretraining.py" \
        --model-name "$MODEL" --data-dir "$DATA_DIR" \
        --output-dir "$out_dir" --strategy "$strategy" \
        --seed "$seed" --cache-dir "$CACHE_DIR" $extra_args

    echo "  Evaluating..."
    python3 "${SCRIPTS_DIR}/exp006_evaluate.py" \
        --model-name "$MODEL" \
        --adapter-path "${out_dir}/final_adapter" \
        --output "$result_file" --cache-dir "$CACHE_DIR"

    sleep 3
}

idx=0
failed=0
for strategy in $STRATEGIES; do
    if [ "$strategy" = "graduated" ]; then
        for alpha in $ALPHAS; do
            for seed in $SEEDS; do
                idx=$((idx + 1))
                tag="${strategy}_a${alpha}_s${seed}"
                echo "[$idx/$total_runs] $tag"
                if ! run_one "$strategy" "$seed" "$alpha" "$tag"; then
                    echo "FAILED: $tag" | tee -a "${OUTPUT_BASE}/failures.log"
                    failed=$((failed + 1))
                fi
            done
        done
    else
        for seed in $SEEDS; do
            idx=$((idx + 1))
            tag="${strategy}_s${seed}"
            echo "[$idx/$total_runs] $tag"
            if ! run_one "$strategy" "$seed" "0" "$tag"; then
                echo "FAILED: $tag" | tee -a "${OUTPUT_BASE}/failures.log"
                failed=$((failed + 1))
            fi
        done
    fi
done

echo ""
echo "=== Complete: $((total_runs - failed))/$total_runs succeeded ==="
if [ $failed -gt 0 ]; then
    echo "Failures logged in ${OUTPUT_BASE}/failures.log"
fi
echo "Run analysis: python3 ${SCRIPTS_DIR}/exp006_analyze.py --results-dir ${OUTPUT_BASE}"
