#!/bin/bash
source $CONDA_PREFIX/etc/profile.d/conda.sh && conda activate base
cd .

export CUDA_VISIBLE_DEVICES=0

python -m src.inference.run_experiment \
    --design design_matrix_exp003_3b.csv \
    --items data/mmlu_items_exp001.json \
    --benchmark mmlu \
    --precision bfloat16 \
    --gpu-id 0 \
    --tensor-parallel 1 \
    --output results/exp003_scale_3b_mmlu.jsonl

echo "DONE: exp003_scale_3b exit_code=$?"
