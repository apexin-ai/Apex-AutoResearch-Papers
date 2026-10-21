#!/bin/bash
# D&R eval commands — prepared 2026-05-24
# Run from /root/provenance_weight_training/
# Each experiment needs 3 evals: holdout, owt, wiki
# Training GPUs: q03→cuda:3, q05→cuda:2, q07→cuda:1
# After training finishes on each GPU, run eval on the same GPU.

EVAL_SCRIPT="eval_perplexity.py"
HOLDOUT="data/human/eval_holdout.jsonl"
OWT="data/eval_openwebtext.jsonl"
WIKI="data/eval_wikipedia.jsonl"
RESULTS_DIR="/root/autodl-tmp/provenance_weight_training/output/eval_results"

# ============================================================
# detect_remove_q03_seed42 (training on cuda:3, max_steps=6103)
# ============================================================
CKPT_Q03="/root/autodl-tmp/provenance_weight_training/output/models/detect_remove_q03_seed42/final"

# holdout
CUDA_VISIBLE_DEVICES=3 python $EVAL_SCRIPT \
  --checkpoints $CKPT_Q03 \
  --data_path $HOLDOUT \
  --max_docs 5000 --max_length 2048 \
  --output_path ${RESULTS_DIR}/detect_remove_q03_seed42_holdout.json

# owt
CUDA_VISIBLE_DEVICES=3 python $EVAL_SCRIPT \
  --checkpoints $CKPT_Q03 \
  --data_path $OWT \
  --max_docs 5000 --max_length 2048 \
  --output_path ${RESULTS_DIR}/detect_remove_q03_seed42_owt.json

# wiki
CUDA_VISIBLE_DEVICES=3 python $EVAL_SCRIPT \
  --checkpoints $CKPT_Q03 \
  --data_path $WIKI \
  --max_docs 5000 --max_length 2048 \
  --output_path ${RESULTS_DIR}/detect_remove_q03_seed42_wiki.json

# ============================================================
# detect_remove_q05_seed42 (training on cuda:2, max_steps=8477)
# ============================================================
CKPT_Q05="/root/autodl-tmp/provenance_weight_training/output/models/detect_remove_q05_seed42/final"

# holdout
CUDA_VISIBLE_DEVICES=2 python $EVAL_SCRIPT \
  --checkpoints $CKPT_Q05 \
  --data_path $HOLDOUT \
  --max_docs 5000 --max_length 2048 \
  --output_path ${RESULTS_DIR}/detect_remove_q05_seed42_holdout.json

# owt
CUDA_VISIBLE_DEVICES=2 python $EVAL_SCRIPT \
  --checkpoints $CKPT_Q05 \
  --data_path $OWT \
  --max_docs 5000 --max_length 2048 \
  --output_path ${RESULTS_DIR}/detect_remove_q05_seed42_owt.json

# wiki
CUDA_VISIBLE_DEVICES=2 python $EVAL_SCRIPT \
  --checkpoints $CKPT_Q05 \
  --data_path $WIKI \
  --max_docs 5000 --max_length 2048 \
  --output_path ${RESULTS_DIR}/detect_remove_q05_seed42_wiki.json

# ============================================================
# detect_remove_q07_seed42 (training on cuda:1, max_steps=6103)
# ============================================================
CKPT_Q07="/root/autodl-tmp/provenance_weight_training/output/models/detect_remove_q07_seed42/final"

# holdout
CUDA_VISIBLE_DEVICES=1 python $EVAL_SCRIPT \
  --checkpoints $CKPT_Q07 \
  --data_path $HOLDOUT \
  --max_docs 5000 --max_length 2048 \
  --output_path ${RESULTS_DIR}/detect_remove_q07_seed42_holdout.json

# owt
CUDA_VISIBLE_DEVICES=1 python $EVAL_SCRIPT \
  --checkpoints $CKPT_Q07 \
  --data_path $OWT \
  --max_docs 5000 --max_length 2048 \
  --output_path ${RESULTS_DIR}/detect_remove_q07_seed42_owt.json

# wiki
CUDA_VISIBLE_DEVICES=1 python $EVAL_SCRIPT \
  --checkpoints $CKPT_Q07 \
  --data_path $WIKI \
  --max_docs 5000 --max_length 2048 \
  --output_path ${RESULTS_DIR}/detect_remove_q07_seed42_wiki.json
