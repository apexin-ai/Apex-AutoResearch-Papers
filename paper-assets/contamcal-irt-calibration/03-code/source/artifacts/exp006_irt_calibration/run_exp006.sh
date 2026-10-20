#!/usr/bin/env bash
# exp-006: IRT Calibration & Baselines orchestration
# Fits IRT models + 7 baselines on each benchmark, then evaluates

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
DATA_DIR="${DATA_DIR:-/root/contamcal-irt-calibration/data}"
OUTPUT_DIR="${OUTPUT_DIR:-/root/contamcal-irt-calibration/results/exp006}"
BENCHMARKS="${BENCHMARKS:-mmlu,gsm8k,arc_challenge,humaneval}"

mkdir -p "$OUTPUT_DIR"

echo "=== exp-006: IRT Calibration & Baselines ==="
echo "Data dir: $DATA_DIR"
echo "Output dir: $OUTPUT_DIR"
echo "Benchmarks: $BENCHMARKS"
echo ""

IFS=',' read -ra BENCH_LIST <<< "$BENCHMARKS"

for bench in "${BENCH_LIST[@]}"; do
    echo "=========================================="
    echo "Benchmark: $bench"
    echo "=========================================="

    RESPONSE="${DATA_DIR}/${bench}/response_matrix.npy"
    EXPOSURE="${DATA_DIR}/${bench}/exposure_matrix.npy"
    GT="${DATA_DIR}/${bench}/ground_truth.json"
    BENCH_OUT="${OUTPUT_DIR}/${bench}"
    mkdir -p "$BENCH_OUT"

    if [ ! -f "$RESPONSE" ] || [ ! -f "$EXPOSURE" ]; then
        echo "WARNING: data files not found for $bench, skipping"
        continue
    fi

    # 1. Fit 4PL+γ with analytical measurement error (scalable to MMLU 14K items)
    echo "--- Fitting 4PL+γ ME (analytic) ---"
    python3 "$SCRIPT_DIR/fit_irt.py" \
        --response-matrix "$RESPONSE" \
        --exposure-matrix "$EXPOSURE" \
        --benchmark "$bench" \
        --output-dir "$BENCH_OUT" \
        --model-type me_analytic \
        --adapt-delta 0.95

    # 1b. For small benchmarks (humaneval), also fit full latent-τ ME as validation
    if [[ "$bench" == "humaneval" ]]; then
        echo "--- Fitting 4PL+γ ME (full latent τ, validation) ---"
        python3 "$SCRIPT_DIR/fit_irt.py" \
            --response-matrix "$RESPONSE" \
            --exposure-matrix "$EXPOSURE" \
            --benchmark "$bench" \
            --output-dir "$BENCH_OUT" \
            --model-type me \
            --adapt-delta 0.95
    fi

    # 2. Fit 4PL+γ simple (ablation, no ME)
    echo "--- Fitting 4PL+γ simple ---"
    python3 "$SCRIPT_DIR/fit_irt.py" \
        --response-matrix "$RESPONSE" \
        --exposure-matrix "$EXPOSURE" \
        --benchmark "$bench" \
        --output-dir "$BENCH_OUT" \
        --model-type simple \
        --adapt-delta 0.95

    # 3. Compute all baselines
    echo "--- Computing baselines ---"
    python3 "$SCRIPT_DIR/compute_baselines.py" \
        --response-matrix "$RESPONSE" \
        --exposure-scores "$EXPOSURE" \
        --benchmark "$bench" \
        --output-dir "$BENCH_OUT"

    # 4. Evaluate all methods
    if [ -f "$GT" ]; then
        echo "--- Evaluating calibration ---"
        IRT_FILES=("$BENCH_OUT/${bench}_me_analytic_results.json" "$BENCH_OUT/${bench}_simple_results.json")
        if [ -f "$BENCH_OUT/${bench}_me_results.json" ]; then
            IRT_FILES+=("$BENCH_OUT/${bench}_me_results.json")
        fi
        python3 "$SCRIPT_DIR/evaluate_calibration.py" \
            --irt-results "${IRT_FILES[@]}" \
            --baseline-results "$BENCH_OUT/${bench}_baselines.json" \
            --ground-truth "$GT" \
            --benchmark "$bench" \
            --output-dir "$BENCH_OUT"
    else
        echo "WARNING: ground truth not found at $GT, skipping evaluation"
    fi

    echo ""
done

echo "=== Aggregating results ==="
python3 -c "
import json, os, glob
output_dir = '$OUTPUT_DIR'
benchmarks = '$BENCHMARKS'.split(',')
summary = {}
for bench in benchmarks:
    eval_path = os.path.join(output_dir, bench, f'{bench}_evaluation.json')
    if os.path.exists(eval_path):
        with open(eval_path) as f:
            summary[bench] = json.load(f)
    else:
        summary[bench] = 'not available'
with open(os.path.join(output_dir, 'exp006_summary.json'), 'w') as f:
    json.dump(summary, f, indent=2)
print(f'Summary written to {output_dir}/exp006_summary.json')
"

echo "=== exp-006 complete ==="
