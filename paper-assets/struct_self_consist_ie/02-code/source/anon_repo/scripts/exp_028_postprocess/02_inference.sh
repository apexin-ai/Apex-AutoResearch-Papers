#!/bin/bash
# N=8 inference with logprobs on Few-NERD 5000-instance subset
# Input: merged model + test data
# Output: output/exp_028_fewnerd_5epoch/samples.jsonl
set -e

source /root/miniconda3/bin/activate
cd /root/autodl-tmp/struct_self_consist_ie

export CUDA_VISIBLE_DEVICES=0

MODEL_PATH="checkpoints/qwen3-8b-fewnerd-5epoch-merged"
DATA_DIR="data/fewnerd_n16_subset"
OUTPUT_DIR="output/exp_028_fewnerd_5epoch"

echo "Running N=8 inference with logprobs..."
echo "  Model: ${MODEL_PATH}"
echo "  Data: ${DATA_DIR}/test.json"
echo "  Output: ${OUTPUT_DIR}/"

python code/run_mvp_pilot.py \
    --model_path "${MODEL_PATH}" \
    --data_dir "${DATA_DIR}" \
    --dataset fewnerd \
    --subtask ner \
    --n_samples 8 \
    --temperature 1.0 \
    --seed 42 \
    --collect_logprobs \
    --num_test 9999 \
    --output_dir "${OUTPUT_DIR}" \
    --tensor_parallel 1

echo "Inference complete."
ls -la "${OUTPUT_DIR}/samples.jsonl"
echo "Done."
