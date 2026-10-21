#!/bin/bash
set +e
source /etc/network_turbo 2>/dev/null || true
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
export HF_HOME=/root/autodl-tmp/.hf_cache
export TOKENIZERS_PARALLELISM=false
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt
export HF_HUB_DISABLE_XET=1
export CUDA_VISIBLE_DEVICES=3
cd /root/contamcal-irt-calibration/exp001

declare -A CKPT_DIRS
CKPT_DIRS[d000]="/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s123"
CKPT_DIRS[d005]="/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s123"
CKPT_DIRS[d025]="/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s123"
CKPT_DIRS[d100]="/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d100_s123"

FAIL_COUNT=0
for DOSE in d000 d005 d025 d100; do
  CKPT="${CKPT_DIRS[$DOSE]}"
  OUT_DIR="/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_${DOSE}_s123_para_aligned"

  if [ -f "${OUT_DIR}/eval_results.json" ]; then
    echo "SKIP ${DOSE} — already exists at ${OUT_DIR}"
    continue
  fi

  echo "=== Running 1.5B ${DOSE} s123 para_aligned eval ==="
  echo "Checkpoint: ${CKPT}"
  echo "Output: ${OUT_DIR}"

  python evaluate.py \
    --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B \
    --adapter-path "${CKPT}/lora_adapter" \
    --output-dir "${OUT_DIR}" \
    --benchmarks mmlu gsm8k arc_challenge humaneval \
    --mc-format aligned \
    --paraphrase-dir /root/autodl-tmp/exp001/paraphrases \
    --cache-dir /root/autodl-tmp/.hf_cache

  if [ $? -ne 0 ]; then
    echo "FAILED ${DOSE}"
    FAIL_COUNT=$((FAIL_COUNT + 1))
  else
    echo "=== Done 1.5B ${DOSE} s123 para_aligned ==="
  fi
done

if [ $FAIL_COUNT -eq 0 ]; then
  echo "ALL_DONE"
else
  echo "COMPLETED_WITH_${FAIL_COUNT}_FAILURES"
fi
