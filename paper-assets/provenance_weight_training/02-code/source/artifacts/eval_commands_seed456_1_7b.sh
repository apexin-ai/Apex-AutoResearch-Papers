#!/bin/bash
# =============================================================================
# Eval commands for 1.7B seed456 (uniform + adaptive)
# 4 GPU parallel: cuda:0-3
# Run from: /root/provenance_weight_training
# Prereq: training must be complete (final/ directory exists)
# =============================================================================

set -e
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
export HF_HOME=/root/autodl-tmp/.hf_cache

cd /root/provenance_weight_training

MODEL_BASE="/root/autodl-tmp/provenance_weight_training/output/models"
UNIFORM_DIR="${MODEL_BASE}/uniform_1_7b_seed456"
ADAPTIVE_DIR="${MODEL_BASE}/adaptive_1_7b_seed456"
UNIFORM="${UNIFORM_DIR}/final"
ADAPTIVE="${ADAPTIVE_DIR}/final"
UNIFORM_EVAL="${UNIFORM_DIR}/eval_results"
ADAPTIVE_EVAL="${ADAPTIVE_DIR}/eval_results"
mkdir -p "$UNIFORM_EVAL" "$ADAPTIVE_EVAL"

# --- Sanity check: ensure training is complete ---
for CKPT in "$UNIFORM" "$ADAPTIVE"; do
    if [ ! -f "${CKPT}/model.safetensors" ]; then
        echo "ERROR: ${CKPT}/model.safetensors not found. Training not complete?"
        exit 1
    fi
done
echo "Both checkpoints found. Starting eval..."

# =============================================================================
# GPU 0: uniform_1_7b_seed456 — holdout PPL + OOD PPL
# =============================================================================
(
    echo "[$(date)] GPU 0: uniform holdout PPL"
    CUDA_VISIBLE_DEVICES=0 python -u eval_perplexity.py \
        --checkpoints "$UNIFORM" \
        --data_path data/human/eval_holdout.jsonl \
        --max_docs 5000 --max_length 2048 \
        --output_path "${UNIFORM_EVAL}/ppl_holdout.json"

    echo "[$(date)] GPU 0: uniform OOD openwebtext"
    CUDA_VISIBLE_DEVICES=0 python -u eval_perplexity.py \
        --checkpoints "$UNIFORM" \
        --data_path data/eval_openwebtext.jsonl \
        --max_docs 5000 --max_length 2048 \
        --output_path "${UNIFORM_EVAL}/ppl_openwebtext.json"

    echo "[$(date)] GPU 0: uniform OOD wikipedia"
    CUDA_VISIBLE_DEVICES=0 python -u eval_perplexity.py \
        --checkpoints "$UNIFORM" \
        --data_path data/eval_wikipedia.jsonl \
        --max_docs 5000 --max_length 2048 \
        --output_path "${UNIFORM_EVAL}/ppl_wikipedia.json"

    echo "[$(date)] GPU 0: ALL DONE"
) > /tmp/eval_seed456_gpu0.log 2>&1 &
PID0=$!

# =============================================================================
# GPU 1: adaptive_1_7b_seed456 — holdout PPL + OOD PPL
# =============================================================================
(
    echo "[$(date)] GPU 1: adaptive holdout PPL"
    CUDA_VISIBLE_DEVICES=1 python -u eval_perplexity.py \
        --checkpoints "$ADAPTIVE" \
        --data_path data/human/eval_holdout.jsonl \
        --max_docs 5000 --max_length 2048 \
        --output_path "${ADAPTIVE_EVAL}/ppl_holdout.json"

    echo "[$(date)] GPU 1: adaptive OOD openwebtext"
    CUDA_VISIBLE_DEVICES=1 python -u eval_perplexity.py \
        --checkpoints "$ADAPTIVE" \
        --data_path data/eval_openwebtext.jsonl \
        --max_docs 5000 --max_length 2048 \
        --output_path "${ADAPTIVE_EVAL}/ppl_openwebtext.json"

    echo "[$(date)] GPU 1: adaptive OOD wikipedia"
    CUDA_VISIBLE_DEVICES=1 python -u eval_perplexity.py \
        --checkpoints "$ADAPTIVE" \
        --data_path data/eval_wikipedia.jsonl \
        --max_docs 5000 --max_length 2048 \
        --output_path "${ADAPTIVE_EVAL}/ppl_wikipedia.json"

    echo "[$(date)] GPU 1: ALL DONE"
) > /tmp/eval_seed456_gpu1.log 2>&1 &
PID1=$!

# =============================================================================
# GPU 2: uniform_1_7b_seed456 — downstream (lm_eval)
# =============================================================================
(
    echo "[$(date)] GPU 2: uniform downstream"
    CUDA_VISIBLE_DEVICES=2 python -m lm_eval \
        --model hf \
        --model_args pretrained=${UNIFORM},dtype=float16 \
        --tasks arc_easy,arc_challenge,hellaswag,piqa,winogrande \
        --batch_size auto \
        --num_fewshot 0 \
        --output_path "${UNIFORM_EVAL}/downstream/"

    echo "[$(date)] GPU 2: ALL DONE"
) > /tmp/eval_seed456_gpu2.log 2>&1 &
PID2=$!

# =============================================================================
# GPU 3: adaptive_1_7b_seed456 — downstream (lm_eval)
# =============================================================================
(
    echo "[$(date)] GPU 3: adaptive downstream"
    CUDA_VISIBLE_DEVICES=3 python -m lm_eval \
        --model hf \
        --model_args pretrained=${ADAPTIVE},dtype=float16 \
        --tasks arc_easy,arc_challenge,hellaswag,piqa,winogrande \
        --batch_size auto \
        --num_fewshot 0 \
        --output_path "${ADAPTIVE_EVAL}/downstream/"

    echo "[$(date)] GPU 3: ALL DONE"
) > /tmp/eval_seed456_gpu3.log 2>&1 &
PID3=$!

# =============================================================================
# Wait and report
# =============================================================================
echo "Launched all 4 GPU eval jobs:"
echo "  GPU 0 (uniform PPL+OOD):      PID=$PID0  log=/tmp/eval_seed456_gpu0.log"
echo "  GPU 1 (adaptive PPL+OOD):     PID=$PID1  log=/tmp/eval_seed456_gpu1.log"
echo "  GPU 2 (uniform downstream):   PID=$PID2  log=/tmp/eval_seed456_gpu2.log"
echo "  GPU 3 (adaptive downstream):  PID=$PID3  log=/tmp/eval_seed456_gpu3.log"
echo ""
echo "Monitor: tail -f /tmp/eval_seed456_gpu*.log"
echo "Check:   ps -p $PID0,$PID1,$PID2,$PID3 -o pid,etime,args"

wait $PID0 $PID1 $PID2 $PID3
echo ""
echo "=========================================="
echo "[$(date)] ALL SEED456 EVALS COMPLETE"
echo "=========================================="
echo ""
echo "Results (eval_results/ pipeline):"
echo "  Uniform:   ${UNIFORM_EVAL}/"
echo "  Adaptive:  ${ADAPTIVE_EVAL}/"
