#!/bin/bash
# D008 Full GSM8K eval — parallel version (2 GPUs)
# cuda:0: RASP models (prune + recovery)
# cuda:1: Standard models (prune + recovery)
# ~2h per eval, ~4h total (2 pairs in parallel)
#
# Usage: bash src/run_full_eval_d008_parallel.sh

set -euo pipefail
cd /root/recovery_aware_struct_prune
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
mkdir -p results

run_rasp() {
    echo "[GPU0] === Post-prune RASP 20% (full 1319) ==="
    CUDA_VISIBLE_DEVICES=0 python src/eval_gsm8k.py \
        --model_path /root/autodl-tmp/pruned_rasp_20 \
        --max_new_tokens 4096 \
        --output_path results/eval_pruned_rasp_20_full.json

    echo "[GPU0] === Post-recovery RASP 20% (full 1319) ==="
    RECOVERED_RASP="/root/autodl-tmp/recovered_rasp_20"
    LATEST_CKPT=$(ls -d ${RECOVERED_RASP}/checkpoint-* 2>/dev/null | sort -t- -k2 -n | tail -1)
    [ -z "$LATEST_CKPT" ] && LATEST_CKPT="$RECOVERED_RASP"
    echo "[GPU0] Using checkpoint: $LATEST_CKPT"
    CUDA_VISIBLE_DEVICES=0 python src/eval_gsm8k.py \
        --model_path "$LATEST_CKPT" \
        --max_new_tokens 4096 \
        --output_path results/eval_recovered_rasp_20_full.json

    echo "[GPU0] === RASP evals done ==="
}

run_standard() {
    echo "[GPU1] === Post-prune Standard 20% (full 1319) ==="
    CUDA_VISIBLE_DEVICES=1 python src/eval_gsm8k.py \
        --model_path /root/autodl-tmp/pruned_standard_20 \
        --max_new_tokens 4096 \
        --output_path results/eval_pruned_standard_20_full.json

    echo "[GPU1] === Post-recovery Standard 20% (full 1319) ==="
    RECOVERED_STD="/root/autodl-tmp/recovered_standard_20"
    LATEST_CKPT=$(ls -d ${RECOVERED_STD}/checkpoint-* 2>/dev/null | sort -t- -k2 -n | tail -1)
    [ -z "$LATEST_CKPT" ] && LATEST_CKPT="$RECOVERED_STD"
    echo "[GPU1] Using checkpoint: $LATEST_CKPT"
    CUDA_VISIBLE_DEVICES=1 python src/eval_gsm8k.py \
        --model_path "$LATEST_CKPT" \
        --max_new_tokens 4096 \
        --output_path results/eval_recovered_standard_20_full.json

    echo "[GPU1] === Standard evals done ==="
}

echo "Starting parallel eval on 2 GPUs..."
run_rasp > >(tee results/eval_d008_gpu0.log) 2>&1 &
PID_RASP=$!
run_standard > >(tee results/eval_d008_gpu1.log) 2>&1 &
PID_STD=$!

echo "RASP evals PID: $PID_RASP (GPU 0)"
echo "Standard evals PID: $PID_STD (GPU 1)"

wait $PID_RASP
EXIT_RASP=$?
wait $PID_STD
EXIT_STD=$?

echo "=== All done. RASP exit=$EXIT_RASP, Standard exit=$EXIT_STD ==="
