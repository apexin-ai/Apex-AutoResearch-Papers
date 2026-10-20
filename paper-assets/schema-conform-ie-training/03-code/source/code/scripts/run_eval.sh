#!/bin/bash
# One-click evaluation for all 3 MVP groups (A/B/C).
# Run after training completes. Assumes merged LoRA checkpoints exist.
# Usage: bash scripts/run_eval.sh

set -euo pipefail

CODE_DIR="/root/autodl-tmp/schema-conform-ie-training/code"
DATA_DIR="/root/autodl-tmp/data"
OUTPUT_DIR="/root/autodl-tmp/eval_results"
EVAL_DATASETS="scierc_test crossner_politics crossner_science"

MODEL_A="/root/autodl-tmp/output/formal_A/merged"
MODEL_B="/root/autodl-tmp/output/formal_B/merged"
MODEL_BASE="/root/autodl-tmp/models/Qwen/Qwen3.5-9B"

cd "$CODE_DIR"
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
mkdir -p "$OUTPUT_DIR/predictions"

echo "============================================"
echo "  Group A: GRPO + F1 only (baseline)"
echo "============================================"
if [ -d "$MODEL_A" ]; then
    CUDA_VISIBLE_DEVICES=0 python -m src.evaluate \
        --model_path "$MODEL_A" \
        --eval_datasets $EVAL_DATASETS \
        --data_dir "$DATA_DIR" \
        --output_dir "$OUTPUT_DIR/group_A" \
        --model_label group_A_baseline \
        --max_new_tokens 512
else
    echo "[SKIP] Model A not found at $MODEL_A"
fi

echo ""
echo "============================================"
echo "  Group B: GRPO + Conformance + GDPO"
echo "============================================"
if [ -d "$MODEL_B" ]; then
    CUDA_VISIBLE_DEVICES=1 python -m src.evaluate \
        --model_path "$MODEL_B" \
        --eval_datasets $EVAL_DATASETS \
        --data_dir "$DATA_DIR" \
        --output_dir "$OUTPUT_DIR/group_B" \
        --model_label group_B_conformance \
        --max_new_tokens 512
else
    echo "[SKIP] Model B not found at $MODEL_B"
fi

echo ""
echo "============================================"
echo "  Group C: Base model zero-shot"
echo "============================================"
CUDA_VISIBLE_DEVICES=0 python -m src.inference_base \
    --model_name "$MODEL_BASE" \
    --data_dir "$DATA_DIR" \
    --eval_datasets $EVAL_DATASETS \
    --output_dir "$OUTPUT_DIR/base_model" \
    --max_new_tokens 512

echo ""
echo "============================================"
echo "  MVP Results Comparison"
echo "============================================"
python3 -c "
import json, os

output_dir = '$OUTPUT_DIR'
results = {}

# Group A
a_path = os.path.join(output_dir, 'group_A', 'eval_results.json')
if os.path.exists(a_path):
    results['A'] = json.load(open(a_path))

# Group B
b_path = os.path.join(output_dir, 'group_B', 'eval_results.json')
if os.path.exists(b_path):
    results['B'] = json.load(open(b_path))

# Group C
c_path = os.path.join(output_dir, 'base_model', 'base_model_results.json')
if os.path.exists(c_path):
    results['C'] = json.load(open(c_path))

datasets = ['scierc_test', 'crossner_politics', 'crossner_science']
metrics = ['f1_correctness', 'entity_f1', 'relation_f1', 'valid_json_rate',
           'conformance_type', 'conformance_relational', 'conformance_completeness']

print(f\"{'Metric':<30} {'A (F1 only)':>12} {'B (conform)':>12} {'C (base)':>12}\")
print('-' * 68)
for ds in datasets:
    print(f'\\n--- {ds} ---')
    for m in metrics:
        row = f'{m:<30}'
        for group in ['A', 'B', 'C']:
            if group in results and ds in results[group] and m in results[group][ds]:
                val = results[group][ds][m]['mean']
                row += f'{val:>12.4f}'
            else:
                row += f'{\"N/A\":>12}'
        print(row)
print()
"

echo "Evaluation complete. Results in $OUTPUT_DIR/"
