#!/bin/bash
set -e
export CUDA_HOME=/root/miniconda3/lib/python3.12/site-packages/nvidia/cu13
export FLASHINFER_DISABLE_VERSION_CHECK=1
source /root/miniconda3/etc/profile.d/conda.sh
conda activate base
cd /root/schema-dag-extraction

MODEL=/root/autodl-tmp/.hf_cache/llama-3.3-70b-instruct-fp8/
COMMON="--dataset fewnerd --prompt_version v2 --types_file configs/few_nerd_types.json --embeddings_path artifacts/type_embeddings.pt --sim_matrix_path artifacts/sim_matrix.pt --model_path $MODEL --max_samples 1000 --max_model_len 4096 --output_dir artifacts/exp012"

mkdir -p artifacts/exp012

echo "===== [$(date)] exp-012 exp1: Count Baseline (LLaMA-3.3-70B-FP8) ====="
python3 src/run_experiment.py --mode exp1 $COMMON

echo "===== [$(date)] exp-012 exp2: Confusability Controlled (LLaMA-3.3-70B-FP8) ====="
python3 src/run_experiment.py --mode exp2 $COMMON

echo "===== [$(date)] exp-012 DONE ====="
