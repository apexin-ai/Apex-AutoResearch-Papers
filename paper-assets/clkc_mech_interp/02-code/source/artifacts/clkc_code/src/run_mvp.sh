#!/bin/bash
# MVP 完整 pipeline：验证 → 翻译 → COMET gate → 激活收集 → 探针训练
# 用法: bash src/run_mvp.sh [--model MODEL] [--data_dir DIR] [--output_dir DIR] [--batch_size N]
set -e

MODEL="${MODEL:-Qwen/Qwen3-8B-Instruct}"
DATA_DIR="${DATA_DIR:-data}"
OUTPUT_DIR="${OUTPUT_DIR:-outputs}"
BATCH_SIZE="${BATCH_SIZE:-4}"

while [[ $# -gt 0 ]]; do
    case $1 in
        --model) MODEL="$2"; shift 2 ;;
        --data_dir) DATA_DIR="$2"; shift 2 ;;
        --output_dir) OUTPUT_DIR="$2"; shift 2 ;;
        --batch_size) BATCH_SIZE="$2"; shift 2 ;;
        *) echo "Unknown arg: $1"; exit 1 ;;
    esac
done

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
mkdir -p "$OUTPUT_DIR"

echo "=============================="
echo "MVP Pipeline (5 steps)"
echo "Model:      $MODEL"
echo "Data dir:   $DATA_DIR"
echo "Output dir: $OUTPUT_DIR"
echo "Batch size: $BATCH_SIZE"
echo "=============================="

echo ""
echo "========== Step 1/5: Verify Parametric Knowledge =========="
python "$SCRIPT_DIR/verify_parametric_knowledge.py" \
    --model "$MODEL" \
    --data_dir "$DATA_DIR" \
    --raw_dir "$DATA_DIR" \
    --output_dir "$DATA_DIR"

echo ""
echo "========== Step 2/5: Translate to ZH =========="
python "$SCRIPT_DIR/translate_to_zh.py" \
    --model "$MODEL" \
    --input_dir "$DATA_DIR" \
    --output_dir "$DATA_DIR" \
    --batch_size "$BATCH_SIZE"

echo ""
echo "========== Step 3/5: Validate Translation (COMET gate) =========="
python "$SCRIPT_DIR/validate_translation.py" \
    --model "$MODEL" \
    --zh_dir "$DATA_DIR" \
    --en_dir "$DATA_DIR" \
    --output_dir "$DATA_DIR"

echo ""
echo "========== Step 4/5: Collect Activations =========="
python "$SCRIPT_DIR/collect_activations.py" \
    --model "$MODEL" \
    --data_dir "$DATA_DIR" \
    --output_dir "$OUTPUT_DIR" \
    --lang en \
    --batch_size "$BATCH_SIZE"

python "$SCRIPT_DIR/collect_activations.py" \
    --model "$MODEL" \
    --data_dir "$DATA_DIR" \
    --output_dir "$OUTPUT_DIR" \
    --lang zh \
    --batch_size "$BATCH_SIZE"

echo ""
echo "========== Step 5/5: Train Probes =========="
python "$SCRIPT_DIR/train_probe.py" \
    --activation_dir "$OUTPUT_DIR" \
    --output_dir "$OUTPUT_DIR"

echo ""
echo "========== MVP Pipeline Complete =========="
echo "Results in $OUTPUT_DIR/"
