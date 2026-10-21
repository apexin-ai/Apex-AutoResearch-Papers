#!/bin/bash
set -e

echo "=== Post exp-002 Master Pipeline ==="
echo "Started: $(date)"

cd .
source $CONDA_PREFIX/etc/profile.d/conda.sh && conda activate base
export PYTHONPATH=.:$PYTHONPATH
export VLLM_USE_V1=0

# Step 1: Validate 16 JSONL files (4 benchmarks × 4 models)
echo ""
echo "--- Step 1: Validating JSONL files ---"
EXPECTED=57600
PASS=0
FAIL=0
for BM in mmlu gsm8k arc hellaswag; do
    for MODEL in qwen llama gemma mistral; do
        f="results/exp002/${MODEL}_${BM}.jsonl"
        if [ ! -f "$f" ]; then
            echo "  MISSING: $f"
            FAIL=$((FAIL + 1))
            continue
        fi
        COUNT=$(wc -l < "$f")
        if [ "$COUNT" -eq "$EXPECTED" ]; then
            echo "  OK: $f ($COUNT records)"
            PASS=$((PASS + 1))
        else
            echo "  FAIL: $f ($COUNT / $EXPECTED records)"
            FAIL=$((FAIL + 1))
        fi
    done
done
echo "Validation: $PASS passed, $FAIL failed out of 16 files"
if [ "$FAIL" -gt 0 ]; then
    echo "ERROR: Some files incomplete. Aborting."
    exit 1
fi

# Step 2: Run 6 analysis scripts serially
echo ""
echo "--- Step 2: Running 6 analysis scripts ---"
SCRIPTS=(
    "per_benchmark_gstudy.py"
    "gradient_permutation_test.py"
    "leave_one_benchmark_out.py"
    "within_format_gradient.py"
    "gsm8k_answer_reextract.py"
    "cross_benchmark_dstudy.py"
)
for script in "${SCRIPTS[@]}"; do
    echo ""
    echo "  Running: $script ($(date +%H:%M:%S))"
    python scripts/exp002_analysis/"$script" 2>&1 | tail -5
    echo "  Done: $script ($(date +%H:%M:%S))"
done

# Step 3: Generate MATH shards and launch inference on 4 GPUs
echo ""
echo "--- Step 3: Launching MATH benchmark ---"

# Generate per-model MATH shards from full design matrix
python3 -c "
import pandas as pd
dm = pd.read_csv('/tmp/design_matrix_exp002_with_math.csv')
math_df = dm[dm['benchmark'] == 'math']
model_map = {
    'Qwen/Qwen3-8B': 'qwen',
    'meta-llama/Llama-3.1-8B-Instruct': 'llama',
    'google/gemma-2-9b-it': 'gemma',
    'mistralai/Mistral-7B-Instruct-v0.3': 'mistral',
}
for model_full, model_short in model_map.items():
    shard = math_df[math_df['model'] == model_full]
    out = f'results/exp002/shard_{model_short}_math.csv'
    shard.to_csv(out, index=False)
    print(f'  {out}: {len(shard)} conditions')
assert len(math_df) == 4 * 288, f'Expected 1152 MATH conditions, got {len(math_df)}'
print('  MATH shards generated OK')
"

# Launch MATH inference — one model per GPU
MODEL_NAMES=("qwen" "llama" "gemma" "mistral")
for gpu in 0 1 2 3; do
    MODEL=${MODEL_NAMES[$gpu]}
    echo "  Starting MATH for ${MODEL} on GPU ${gpu}"
    CUDA_VISIBLE_DEVICES=$gpu nohup python -m src.inference.run_experiment \
        --design "results/exp002/shard_${MODEL}_math.csv" \
        --benchmark math \
        --gpu-id 0 \
        --output "results/exp002/${MODEL}_math.jsonl" \
        > "results/exp002/gpu${gpu}_${MODEL}_math.log" 2>&1 &
    echo "  PID: $!"
done

echo ""
echo "=== Pipeline complete. MATH inference launched on 4 GPUs. ==="
echo "Monitor: tail -f results/exp002/gpu*_math.log"
echo "Finished: $(date)"
