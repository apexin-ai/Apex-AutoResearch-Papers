#!/bin/bash
# exp-003: Decoding Strategy Ablation on Qwen2.5-1.5B-Instruct
# 4 configurations, each saves to separate data/results dirs
# Usage: bash scripts/run_exp003_ablation.sh <config_num>
#   1 = greedy
#   2 = nucleus p=0.9, T=1.0
#   3 = nucleus p=0.95, T=0.7
#   4 = nucleus p=0.95, T=1.2

source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
source /etc/network_turbo 2>/dev/null
export HF_HOME=/root/autodl-tmp/.hf_cache
export HF_HUB_DISABLE_XET=1
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt
export HF_ENDPOINT=https://hf-mirror.com

MODEL=/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B-Instruct/Qwen/Qwen2.5-1.5B-Instruct
BASE=/root/autodl-tmp/gen-depth-contamination
SCRIPT=$BASE/scripts/run_pipeline.py
N=5000
D=5

case "$1" in
  1)
    DESC="greedy"
    python $SCRIPT --model_path $MODEL --data_dir $BASE/data_exp003_greedy --results_dir $BASE/results_exp003_greedy --num_samples $N --max_depth $D --no_sample
    ;;
  2)
    DESC="nucleus_p0.9_t1.0"
    python $SCRIPT --model_path $MODEL --data_dir $BASE/data_exp003_nuc09 --results_dir $BASE/results_exp003_nuc09 --num_samples $N --max_depth $D --top_p 0.9 --temperature 1.0
    ;;
  3)
    DESC="nucleus_p0.95_t0.7"
    python $SCRIPT --model_path $MODEL --data_dir $BASE/data_exp003_t07 --results_dir $BASE/results_exp003_t07 --num_samples $N --max_depth $D --top_p 0.95 --temperature 0.7
    ;;
  4)
    DESC="nucleus_p0.95_t1.2"
    python $SCRIPT --model_path $MODEL --data_dir $BASE/data_exp003_t12 --results_dir $BASE/results_exp003_t12 --num_samples $N --max_depth $D --top_p 0.95 --temperature 1.2
    ;;
  *)
    echo "Usage: $0 {1|2|3|4}"
    exit 1
    ;;
esac
echo "Completed: $DESC"
