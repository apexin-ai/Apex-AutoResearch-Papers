#!/bin/bash
set -e
source /root/miniconda3/bin/activate
cd /root/autodl-tmp/struct_self_consist_ie

export CUDA_VISIBLE_DEVICES=1

echo "=== $(date) === Starting Few-NERD seed=123 inference ==="

python code/run_mvp_pilot.py \
    --model_path output/exp_021_fewnerd_full \
    --data_dir data/fewnerd \
    --dataset fewnerd \
    --subtask ner \
    --n_samples 8 \
    --temperature 1.0 \
    --seed 123 \
    --collect_logprobs \
    --output_dir output/exp_021_fewnerd_n8_seed123

echo "=== $(date) === Inference done, running analysis ==="

python code/analyze_fewnerd_results.py \
    --input_dir output/exp_021_fewnerd_n8_seed123 \
    --output_dir output/exp_021_fewnerd_n8_seed123

echo "=== $(date) === All done ==="
