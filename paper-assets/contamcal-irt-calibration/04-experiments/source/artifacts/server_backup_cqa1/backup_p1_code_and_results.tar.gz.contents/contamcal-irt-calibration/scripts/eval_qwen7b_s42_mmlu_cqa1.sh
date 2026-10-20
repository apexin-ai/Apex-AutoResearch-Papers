#!/bin/bash
set -e -x

# C009: evaluate.py md5 verification
EXPECTED_MD5="17673bf373f00f83ccc41fc1d355a4cd"
ACTUAL_MD5=$(md5sum /root/contamcal-irt-calibration/exp001/evaluate.py | cut -d' ' -f1)
if [ "$ACTUAL_MD5" != "$EXPECTED_MD5" ]; then
  echo "ERROR: evaluate.py md5 mismatch! Expected $EXPECTED_MD5, got $ACTUAL_MD5"
  exit 1
fi

# C004: explicit CUDA_VISIBLE_DEVICES
export CUDA_VISIBLE_DEVICES=0
export HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache

PYTHON=/root/miniconda3/bin/python
EVAL=/root/contamcal-irt-calibration/exp001/evaluate.py
CKPT=/root/autodl-tmp/exp001/checkpoints
MODEL=/root/autodl-tmp/models/Qwen2.5-7B/Qwen/Qwen2___5-7B
OUT=/root/contamcal-irt-calibration/results_mmlu_s42

run_eval() {
  local name=$1 adapter=$2 outdir=$3
  if [ ! -f "$adapter/adapter_config.json" ]; then
    echo "=== SKIP: $name — adapter not found at $adapter ==="
    return
  fi

  # C006: verify lora_alpha=32
  ALPHA=$(grep -o '"lora_alpha": [0-9]*' "$adapter/adapter_config.json" | grep -o '[0-9]*')
  if [ "$ALPHA" != "32" ]; then
    echo "=== ERROR: $name has lora_alpha=$ALPHA (expected 32), skipping ==="
    return
  fi

  mkdir -p "$outdir"
  echo "=== START: $name at $(date) ==="
  $PYTHON $EVAL \
    --model-path "$MODEL" \
    --adapter-path "$adapter" \
    --benchmarks mmlu \
    --batch-size 8 \
    --output-dir "$outdir"
  echo "=== DONE: $name at $(date), exit=$? ==="
}

for d in 000 005 025 050 100; do
  run_eval "qwen7b_d${d}_s42" "$CKPT/Qwen2.5-7B_d${d}_s42/lora_adapter" "$OUT/d${d}_s42"
done

echo "ALL_MMLU_EVAL_DONE_QWEN7B_S42"
