#!/bin/bash
source ${CONDA_SH:-$HOME/miniconda3/etc/profile.d/conda.sh}
conda activate base
export PATH=/usr/local/cuda/bin:$PATH
cd ${PROJECT_ROOT:-.}

python3 scripts/eval_composition.py \
  --models \
    ${MODEL_DIR:-./models}/340M-20B-GatedDeltaNet-pure-baseline \
    ${MODEL_DIR:-./models}/340M-20B-GatedDeltaNet-New-hybrid-24-1 \
    ${MODEL_DIR:-./models}/340M-20B-GatedDeltaNet-hybrid-12-1 \
    ${MODEL_DIR:-./models}/340M-20B-GatedDeltaNet-hybrid-6-1 \
    ${MODEL_DIR:-./models}/340M-20B-GatedDeltaNet-hybrid-3-1 \
    ${MODEL_DIR:-./models}/340M-20B-HGRN2-pure-baseline \
    ${MODEL_DIR:-./models}/340M-20B-HGRN2-hybrid-24-1 \
    ${MODEL_DIR:-./models}/340M-20B-HGRN2-hybrid-12-1 \
    ${MODEL_DIR:-./models}/340M-20B-HGRN2-hybrid-6-1 \
    ${MODEL_DIR:-./models}/340M-20B-HGRN2-hybrid-3-1 \
    ${MODEL_DIR:-./models}/340M-20B-RetNet-pure \
    ${MODEL_DIR:-./models}/340M-20B-RetNet-hybrid-24-1 \
    ${MODEL_DIR:-./models}/340M-20B-RetNet-hybrid-12-1 \
    ${MODEL_DIR:-./models}/340M-20B-RetNet-hybrid-6-1 \
    ${MODEL_DIR:-./models}/340M-20B-RetNet-hybrid-3-1 \
    ${MODEL_DIR:-./models}/transformer_340M_baseline \
  --depths 1 2 3 4 5 \
  --num-samples 500 \
  --num-shots 6 \
  --batch-size 64 \
  --output-dir ${PROJECT_ROOT:-.}/results/mvp_direct \
  --variant direct \
  --device cuda
