#!/bin/bash
set -e
source /root/miniconda3/bin/activate
cd /root/autodl-tmp/struct_self_consist_ie

SEED=${1:?Usage: bash run_32b_fewnerd_inference.sh <seed> <gpu_ids> [tp_size]}
GPU_IDS=${2:?Specify GPU IDs, e.g. "0,1"}
TP=${3:-2}

MODEL_PATH="checkpoints/qwen25-32b-fewnerd-merged"
OUTPUT_DIR="output/qwen25_32b_fewnerd_n8_seed${SEED}"
LOG_FILE="logs/32b_fewnerd_seed${SEED}.log"

mkdir -p logs "$(dirname "$OUTPUT_DIR")"

export CUDA_VISIBLE_DEVICES=$GPU_IDS

echo "=== $(date) === 32B FewNERD inference: seed=$SEED gpu=$GPU_IDS tp=$TP ==="

python code/run_mvp_pilot.py \
    --model_path $MODEL_PATH \
    --data_dir data/fewnerd \
    --dataset fewnerd \
    --subtask ner \
    --n_samples 8 \
    --temperature 1.0 \
    --seed $SEED \
    --tensor_parallel $TP \
    --collect_logprobs \
    --output_dir $OUTPUT_DIR

echo "=== $(date) === Inference done, running analysis ==="

python code/analyze_fewnerd_results.py \
    --input_dir $OUTPUT_DIR \
    --output_dir $OUTPUT_DIR

echo "=== $(date) === seed=$SEED complete ==="
