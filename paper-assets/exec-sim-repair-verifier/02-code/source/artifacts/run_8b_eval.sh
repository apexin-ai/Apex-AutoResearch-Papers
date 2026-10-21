#!/bin/bash
# 8B Eval Pipeline — CLS and CWM
# 用法: bash run_8b_eval.sh <gpu_id> <model_type> [max_seq_length]
# 例: bash run_8b_eval.sh 0 cls 6144
#     bash run_8b_eval.sh 1 cwm 6144
#     bash run_8b_eval.sh 2 cls42 6144   # seed42 CLS re-eval

set -e

GPU_ID=${1:?Usage: bash run_8b_eval.sh <gpu_id> <model_type> [max_seq_length]}
MODEL_TYPE=${2:?Specify cls, cwm, or cls42}
MAX_SEQ=${3:-6144}

source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /home/sonny/exec-sim-repair-verifier

export CUDA_VISIBLE_DEVICES=$GPU_ID
BASE_MODEL="/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B"
BATCH_SIZE=1

if [ "$MODEL_TYPE" == "cls" ]; then
    CKPT_DIR="/root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda"
    EVAL_SCRIPT="eval_repo_cls.py"
    RESULTS_DIR="results/8b_cls_seed123"
elif [ "$MODEL_TYPE" == "cwm" ]; then
    CKPT_DIR="/root/autodl-tmp/checkpoints_repo_cwm_8b_conda"
    EVAL_SCRIPT="eval_repo_cwm.py"
    RESULTS_DIR="results/8b_cwm"
elif [ "$MODEL_TYPE" == "cls42" ]; then
    CKPT_DIR="/root/autodl-tmp/checkpoints_repo_cls_8b_conda"
    EVAL_SCRIPT="eval_repo_cls.py"
    RESULTS_DIR="results/8b_cls_seed42"
else
    echo "Unknown model_type: $MODEL_TYPE. Use cls, cwm, or cls42."
    exit 1
fi

mkdir -p $RESULTS_DIR

echo "=== 8B $MODEL_TYPE Eval Pipeline ==="
echo "GPU: $GPU_ID, max_seq_length: $MAX_SEQ, batch_size: $BATCH_SIZE"
echo "Checkpoint dir: $CKPT_DIR"
echo "Results dir: $RESULTS_DIR"
echo ""

for ckpt in $(ls -d $CKPT_DIR/checkpoint-* | sort -t- -k2 -n); do
    ckpt_name=$(basename $ckpt)
    ckpt_num=${ckpt_name#checkpoint-}

    for split in val test; do
        OUT_JSON="${RESULTS_DIR}/${MODEL_TYPE}_${ckpt_name}_${split}.json"
        OUT_PRED="${RESULTS_DIR}/${MODEL_TYPE}_${ckpt_name}_${split}_preds.jsonl"

        if [ -f "$OUT_JSON" ]; then
            echo "SKIP $ckpt_name $split (already exists: $OUT_JSON)"
            continue
        fi

        echo "--- $ckpt_name / $split ---"

        if [ "$EVAL_SCRIPT" == "eval_repo_cwm.py" ]; then
            python3 $EVAL_SCRIPT \
                --checkpoint_dir $ckpt \
                --model_name $BASE_MODEL \
                --device cuda:0 \
                --split $split \
                --max_seq_length $MAX_SEQ \
                --batch_size $BATCH_SIZE \
                --output $OUT_JSON \
                --pred_output $OUT_PRED \
                --output_dir $RESULTS_DIR
        else
            python3 $EVAL_SCRIPT \
                --checkpoint_dir $ckpt \
                --model_name $BASE_MODEL \
                --device cuda:0 \
                --split $split \
                --max_seq_length $MAX_SEQ \
                --batch_size $BATCH_SIZE \
                --output $OUT_JSON \
                --pred_output $OUT_PRED
        fi

        echo "--- $ckpt_name / $split done ---"
        sleep 2
    done
done

echo "=== 8B $MODEL_TYPE Eval Complete ==="
echo "Results:"
ls -la $RESULTS_DIR/
