#!/bin/bash
set -x
cd /root/contamcal-irt-calibration/exp001

MODEL_PATH="/root/autodl-tmp/models/Qwen2.5-7B/Qwen/Qwen2___5-7B"
CKPT_BASE="/root/autodl-tmp/exp001/checkpoints"

for d in 000 005 025 050 100; do
  ADAPTER_PATH="${CKPT_BASE}/Qwen2.5-7B_d${d}_s123/lora_adapter"

  if [ ! -f "${ADAPTER_PATH}/adapter_config.json" ]; then
    echo "SKIP d${d}: adapter not found at ${ADAPTER_PATH}"
    continue
  fi

  echo "=== Eval Qwen-7B d${d} s123 at $(date) ==="
  HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 \
  HF_HOME=/root/autodl-tmp/.hf_cache \
  CUDA_VISIBLE_DEVICES=0 \
  /root/miniconda3/bin/python evaluate.py \
    --model-path ${MODEL_PATH} \
    --adapter-path ${ADAPTER_PATH} \
    --benchmarks mmlu arc_challenge \
    --mc-format aligned \
    --output-dir /root/autodl-tmp/exp001/eval_results_v2/qwen7b_d${d}_s123 \
    --batch-size 4
  echo "=== Done d${d}, exit=$? ==="
done
echo "ALL_EVAL_DONE_QWEN7B_S123_CQA1"
