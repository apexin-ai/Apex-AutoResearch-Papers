#!/bin/bash
# 14B multi-seed bf16 eval script
# Run on seetacloud-westd-4x5090 after all 4 training jobs complete.
# Reads best checkpoint from trainer_state.json (no hardcoded step).

set -euo pipefail

PROJECT_DIR="/home/sonny/exec-sim-repair-verifier"
CKPT_BASE="/root/autodl-tmp/checkpoints"
MODEL_BASE="/dev/shm/Qwen3-14B"
DATA_DIR="${PROJECT_DIR}/data"

# Activate environment
source /root/miniconda3/etc/profile.d/conda.sh
conda activate base
cd "${PROJECT_DIR}"

get_best_checkpoint() {
    local ckpt_dir="$1"
    python3 -c "
import json, os
state_path = os.path.join('${ckpt_dir}', 'trainer_state.json')
with open(state_path) as f:
    state = json.load(f)
best = state.get('best_model_checkpoint', '')
if not best:
    # fallback: use last checkpoint
    import glob
    ckpts = sorted(glob.glob(os.path.join('${ckpt_dir}', 'checkpoint-*')))
    best = ckpts[-1] if ckpts else ''
print(best)
"
}

run_eval() {
    local exp_id="$1"
    local mode="$2"
    local ckpt_dir="$3"
    local gpu="$4"
    local test_file="$5"

    echo "=========================================="
    echo "Evaluating: ${exp_id} (mode=${mode}, GPU=${gpu})"
    echo "=========================================="

    local best_ckpt
    best_ckpt=$(get_best_checkpoint "${ckpt_dir}")

    if [ -z "${best_ckpt}" ]; then
        echo "ERROR: No checkpoint found in ${ckpt_dir}"
        return 1
    fi

    echo "Best checkpoint: ${best_ckpt}"

    CUDA_VISIBLE_DEVICES=${gpu} python3 eval_func_bf16.py \
        --model_name_or_path "${MODEL_BASE}" \
        --adapter_path "${best_ckpt}" \
        --test_file "${DATA_DIR}/${test_file}" \
        --mode "${mode}" \
        --dtype bf16 \
        --batch_size 8 \
        --output_file "artifacts/eval_${exp_id}_bf16.json" \
        2>&1 | tee "logs/eval_${exp_id}_bf16.log"

    echo ""
}

echo "Starting 14B multi-seed bf16 eval..."
echo "Time: $(date)"
echo ""

# ── CLS evals ──────────────────────────────────────────────────────
run_eval "cls14b-func-s123" "cls" "${CKPT_BASE}/cls14b-func-s123" 0 "test.jsonl"
run_eval "cls14b-func-s456" "cls" "${CKPT_BASE}/cls14b-func-s456" 1 "test.jsonl"

# ── CWM evals ──────────────────────────────────────────────────────
run_eval "cwm14b-func-s123" "cwm" "${CKPT_BASE}/cwm14b-func-s123" 2 "cwm_test.jsonl"
run_eval "cwm14b-func-s456" "cwm" "${CKPT_BASE}/cwm14b-func-s456" 3 "cwm_test.jsonl"

echo ""
echo "=========================================="
echo "All evals complete. Time: $(date)"
echo "=========================================="
echo ""
echo "Results:"
for f in artifacts/eval_*14b*bf16.json; do
    echo "  ${f}:"
    python3 -c "import json; d=json.load(open('${f}')); print(f'    accuracy: {d.get(\"accuracy\", d.get(\"acc\", \"?\"))}%')" 2>/dev/null || echo "    (parse manually)"
done

# NOTE: If eval_func_bf16.py doesn't exist, check for alternative names:
#   - eval_cls_14b_bf16.py (used for s42 eval)
#   - run_eval.py --dtype bf16
#   - python3 train_unified.py --eval_only --dtype bf16
# Adapt the run_eval function accordingly.
