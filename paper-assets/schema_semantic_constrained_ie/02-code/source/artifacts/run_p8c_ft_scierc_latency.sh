#!/bin/bash
set -e

cd /root/schema_semantic_constrained_ie

MODEL_PATH="/root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged"
DATA_PATH="data/processed_data/test.json"
CONSTRAINTS_PATH="ontology_constraints.json"
OUTPUT_DIR="/root/autodl-tmp/schema_outputs"
DEVICE="cuda:0"

UNC_OUTPUT="${OUTPUT_DIR}/p8c_timing_ft_unconstrained.jsonl"
CON_OUTPUT="${OUTPUT_DIR}/p8c_timing_ft_constrained.jsonl"

if [ ! -d "$MODEL_PATH" ]; then
    echo "ERROR: Merged model not found at $MODEL_PATH"
    exit 1
fi

echo "=========================================="
echo "P8c: FT SciERC Latency Benchmark"
echo "Model: $MODEL_PATH"
echo "Data: $DATA_PATH"
echo "Device: $DEVICE"
echo "=========================================="

echo ""
echo "[Phase 1/2] Running unconstrained inference..."
echo "Output: $UNC_OUTPUT"
CUDA_VISIBLE_DEVICES=0 python3 run_constrained_extraction.py \
    --mode unconstrained \
    --dataset scierc \
    --model_path "$MODEL_PATH" \
    --data_path "$DATA_PATH" \
    --constraints_path "$CONSTRAINTS_PATH" \
    --output_path "$UNC_OUTPUT" \
    --device cuda:0 \
    --batch_size 1 \
    --max_new_tokens 2048 \
    --seed 42

echo ""
echo "[Phase 2/2] Running constrained (full_s1) inference..."
echo "Output: $CON_OUTPUT"
CUDA_VISIBLE_DEVICES=0 python3 run_constrained_extraction.py \
    --mode full_s1 \
    --dataset scierc \
    --model_path "$MODEL_PATH" \
    --data_path "$DATA_PATH" \
    --constraints_path "$CONSTRAINTS_PATH" \
    --output_path "$CON_OUTPUT" \
    --device cuda:0 \
    --batch_size 1 \
    --max_new_tokens 2048 \
    --seed 42

echo ""
echo "[Analysis] Computing latency overhead..."
python3 analyze_latency.py "$UNC_OUTPUT" "$CON_OUTPUT"

echo ""
echo "=========================================="
UNC_COUNT=$(wc -l < "$UNC_OUTPUT")
CON_COUNT=$(wc -l < "$CON_OUTPUT")

python3 -c "
import json, numpy as np

def load_times(path):
    times = []
    with open(path) as f:
        for line in f:
            d = json.loads(line.strip())
            times.append(d['inference_time_seconds'])
    return np.array(times)

unc = load_times('$UNC_OUTPUT')
con = load_times('$CON_OUTPUT')

unc_mean, unc_med = np.mean(unc), np.median(unc)
con_mean, con_med = np.mean(con), np.median(con)
oh_mean = (con_mean / unc_mean - 1) * 100
oh_med = (con_med / unc_med - 1) * 100

print('=== P8c FT SciERC Latency Summary ===')
print(f'Unconstrained: mean={unc_mean:.3f}s/doc, median={unc_med:.3f}s/doc')
print(f'Constrained:   mean={con_mean:.3f}s/doc, median={con_med:.3f}s/doc')
print(f'Overhead (mean): {oh_mean:+.2f}%')
print(f'Overhead (median): {oh_med:+.2f}%')
print(f'Docs: {len(unc)}')
"
echo "=========================================="
echo "P8c experiment complete."
