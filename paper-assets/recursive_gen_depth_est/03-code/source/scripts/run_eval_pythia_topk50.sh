#!/bin/bash
set -e
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
GPU=${GPU:-0}
export CUDA_VISIBLE_DEVICES=$GPU
cd /root/autodl-tmp/recursive_gen_depth_est

DATA_DIR=data/pythia_topk50
RESULTS_DIR=results/pythia_topk50
MODEL_PATH=/root/autodl-tmp/models/pythia-1.4b
LOG_FILE=logs/eval_pythia_topk50.log
mkdir -p "$RESULTS_DIR/three_class" "$RESULTS_DIR/three_class_filtered" logs

exec > >(tee -a "$LOG_FILE") 2>&1
echo "=== Eval: Pythia topk50 ==="
echo "=== Started at $(date) ==="

echo "=== Step 1: Code contamination ==="
for d in 0 1 2 3; do
    echo "--- depth-$d ---"
    python scripts/filter_code.py --input "$DATA_DIR/depth_$d.jsonl" --mode stats
done

echo "=== Step 2: Feature extraction ==="
python scripts/extract_features.py --data_dir "$DATA_DIR" --model_path "$MODEL_PATH" --output_path "$RESULTS_DIR/features.jsonl" --gpu 0 --batch_size 16

echo "=== Step 3: 4-class classification ==="
python scripts/train_classifier.py --features_path "$RESULTS_DIR/features.jsonl" --output_dir "$RESULTS_DIR"

echo "=== Step 4: 3-class d1d2d3 ==="
python3 scripts/filter_features_d1d3.py "$RESULTS_DIR/features.jsonl" "$RESULTS_DIR/features_3class.jsonl"
python scripts/train_classifier.py --features_path "$RESULTS_DIR/features_3class.jsonl" --output_dir "$RESULTS_DIR/three_class"

echo "=== Step 5: 3-class filtered ==="
for d in 1 2 3; do
    python scripts/filter_code.py --input "$DATA_DIR/depth_$d.jsonl" --mode filter --output "$RESULTS_DIR/depth_${d}_filtered.jsonl"
done
FILTERED_DIR="$RESULTS_DIR/filtered_tmp"
mkdir -p "$FILTERED_DIR"
ln -sf "$(pwd)/$DATA_DIR/depth_0.jsonl" "$FILTERED_DIR/depth_0.jsonl"
for d in 1 2 3; do
    ln -sf "$(pwd)/$RESULTS_DIR/depth_${d}_filtered.jsonl" "$FILTERED_DIR/depth_${d}.jsonl"
done
python scripts/extract_features.py --data_dir "$FILTERED_DIR" --model_path "$MODEL_PATH" --output_path "$RESULTS_DIR/features_filtered.jsonl" --gpu 0 --batch_size 16
python3 scripts/filter_features_d1d3.py "$RESULTS_DIR/features_filtered.jsonl" "$RESULTS_DIR/features_3class_filtered.jsonl"
python scripts/train_classifier.py --features_path "$RESULTS_DIR/features_3class_filtered.jsonl" --output_dir "$RESULTS_DIR/three_class_filtered"
rm -rf "$FILTERED_DIR"

echo "=== Eval complete ==="
echo "=== Finished at $(date) ==="
