#!/bin/bash
# End-to-end reproduction pipeline for cross-lingual knowledge conflict probing.
#
# Prerequisites:
#   - GPU with >= 24GB VRAM (for model inference)
#   - ConflictQA dataset downloaded to data/
#   - Models downloaded or accessible via HuggingFace
#
# Usage:
#   bash scripts/run_pipeline.sh <MODEL_PATH> <MODEL_KEY> <NUM_LAYERS>
#
# Example:
#   bash scripts/run_pipeline.sh meta-llama/Llama-3.1-8B-Instruct llama31 32

set -e

MODEL_PATH=${1:?"Usage: $0 <MODEL_PATH> <MODEL_KEY> <NUM_LAYERS>"}
MODEL_KEY=${2:?"Usage: $0 <MODEL_PATH> <MODEL_KEY> <NUM_LAYERS>"}
NUM_LAYERS=${3:?"Usage: $0 <MODEL_PATH> <MODEL_KEY> <NUM_LAYERS>"}

DATA_DIR="data/${MODEL_KEY}"
XNLI_DIR="data/xnli/${MODEL_KEY}"
RESULTS_DIR="results/${MODEL_KEY}"

mkdir -p "$DATA_DIR" "$XNLI_DIR" "$RESULTS_DIR" logs

echo "=== Step 1: Verify parametric knowledge ==="
python -u src/verify_parametric_knowledge.py \
    --model "$MODEL_PATH" \
    --data_dir data/ \
    --raw_dir data/ \
    --output_dir "$DATA_DIR/"

echo "=== Step 2: Translate to ZH ==="
python -u src/translate.py \
    --model "$MODEL_PATH" \
    --target_lang zh \
    --input_dir "$DATA_DIR/" \
    --output_dir "$DATA_DIR/"

echo "=== Step 3: Validate translations ==="
python -u src/validate_translation.py \
    --model "$MODEL_PATH" \
    --source_lang_dir "$DATA_DIR/" \
    --en_dir "$DATA_DIR/" \
    --output_dir "$DATA_DIR/" \
    --threshold 0.80 \
    --source_lang zh

echo "=== Step 4: Collect activations (EN) ==="
python -u src/collect_activations.py \
    --model "$MODEL_PATH" \
    --data_dir "$DATA_DIR/" \
    --output_dir "$DATA_DIR/" \
    --lang en

echo "=== Step 4b: Collect activations (ZH) ==="
python -u src/collect_activations.py \
    --model "$MODEL_PATH" \
    --data_dir "$DATA_DIR/" \
    --output_dir "$DATA_DIR/" \
    --lang zh

echo "=== Step 5: Train probes ==="
CUDA_VISIBLE_DEVICES="" python -u src/train_probe.py \
    --activation_dir "$DATA_DIR/" \
    --output_dir "$DATA_DIR/" \
    --seeds 42,123,456,789,1024

echo "=== Step 6: Bootstrap probe CIs ==="
CUDA_VISIBLE_DEVICES="" python -u src/bootstrap_probe.py \
    --activation_dir "$DATA_DIR/" \
    --output_dir "$RESULTS_DIR/" \
    --n_bootstrap 2000

echo "=== Step 7: COMET tertile ablation ==="
# Replace BEST_LAYER with the peak layer from probe results
python -u src/comet_tertile_ablation.py \
    --data_dir "$DATA_DIR/" \
    --best_layer 14 \
    --model_name "$MODEL_KEY" \
    --output "$RESULTS_DIR/comet_tertile_ablation.json"

echo "=== Step 8: Random labels control ==="
CUDA_VISIBLE_DEVICES="" python -u src/random_labels_control.py \
    --models "{\"${MODEL_KEY}\": {\"activation_dir\": \"${DATA_DIR}\", \"n_layers\": ${NUM_LAYERS}}}" \
    --output "$RESULTS_DIR/random_labels_control.json"

echo "=== Pipeline complete ==="
echo "Results saved to $RESULTS_DIR/"
