#!/bin/bash
set -e

cd /root/autodl-tmp/gen-depth-contamination
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

PROJ=/root/autodl-tmp/gen-depth-contamination
PYTHIA=/root/autodl-tmp/.hf_cache/EleutherAI/pythia-1.4b
OLMO=/root/autodl-tmp/.hf_cache/allenai/OLMo-1B-hf
DATA_RW=${PROJ}/data
DATA_CONT=${PROJ}/data_exp017_qwen_cont
BASELINE_RW=${PROJ}/results/feature_importance.json
BASELINE_CONT=${PROJ}/results_exp017_qwen_cont/feature_importance.json

echo "========== [1/4] Pythia x Qwen-rewrite =========="
python scripts/exp_A_alt_scorer.py \
  --scorer_model_path $PYTHIA \
  --data_dir $DATA_RW \
  --output_dir ${PROJ}/artifacts/exp_A/pythia_qwen_rw \
  --baseline_importance_json $BASELINE_RW \
  --device cuda:0 --batch_size 8

echo "========== [2/4] Pythia x Qwen-cont =========="
python scripts/exp_A_alt_scorer.py \
  --scorer_model_path $PYTHIA \
  --data_dir $DATA_CONT \
  --output_dir ${PROJ}/artifacts/exp_A/pythia_qwen_cont \
  --baseline_importance_json $BASELINE_CONT \
  --device cuda:0 --batch_size 8

echo "========== [3/4] OLMo x Qwen-rewrite =========="
python scripts/exp_A_alt_scorer.py \
  --scorer_model_path $OLMO \
  --data_dir $DATA_RW \
  --output_dir ${PROJ}/artifacts/exp_A/olmo_qwen_rw \
  --baseline_importance_json $BASELINE_RW \
  --device cuda:0 --batch_size 8

echo "========== [4/4] OLMo x Qwen-cont =========="
python scripts/exp_A_alt_scorer.py \
  --scorer_model_path $OLMO \
  --data_dir $DATA_CONT \
  --output_dir ${PROJ}/artifacts/exp_A/olmo_qwen_cont \
  --baseline_importance_json $BASELINE_CONT \
  --device cuda:0 --batch_size 8

echo "========== ALL 4 RUNS COMPLETE =========="
