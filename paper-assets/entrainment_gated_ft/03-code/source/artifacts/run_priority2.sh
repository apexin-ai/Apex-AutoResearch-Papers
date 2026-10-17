#!/bin/bash
set -eo pipefail
source /etc/network_turbo
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
export HF_HOME=/root/autodl-tmp/.hf_cache
export HF_HUB_DISABLE_XET=1
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt

OUTDIR="/root/entrainment_gated_ft/results/exp005_zoo_expansion"
LOG="$OUTDIR/priority2.log"
MODELS="/root/entrainment_gated_ft/models"

echo "=== Priority 2: Remaining ratios START $(date) ===" | tee "$LOG"

# Model name mapping for pure variants
declare -A PURE_NAMES
PURE_NAMES[GLA]="340M-20B-GLA-pure-baseline"
PURE_NAMES[DeltaNet]="340M-20B-DeltaNet-pure"
PURE_NAMES[HGRN]="340M-20B-HGRN-pure-baseline"

# Priority 2A: New archs remaining ratios
for arch in GLA DeltaNet HGRN; do
  for ratio in pure hybrid-24-1 hybrid-12-1 hybrid-6-1; do
    if [ "$ratio" = "pure" ]; then
      MODEL_NAME="${PURE_NAMES[$arch]}"
    else
      MODEL_NAME="340M-20B-${arch}-${ratio}"
    fi
    MODEL_DIR="$MODELS/$MODEL_NAME"
    OUT_KEY="${arch}_${ratio}"

    # Skip if already evaluated
    if find "$OUTDIR/${OUT_KEY}" -name "samples_lambada_openai_*.jsonl" 2>/dev/null | grep -q .; then
      echo "$OUT_KEY: already done, skipping" | tee -a "$LOG"
      continue
    fi

    # Download if not exists (use ModelScope for speed on AutoDL)
    if [ ! -d "$MODEL_DIR" ] || [ ! -f "$MODEL_DIR/model.safetensors" ]; then
      echo "Downloading $MODEL_NAME via ModelScope..." | tee -a "$LOG"
      mkdir -p "$MODEL_DIR"
      python3 -c "
from modelscope import snapshot_download
import time, shutil, os
t0 = time.time()
cache_dir = '/root/autodl-tmp/.ms_cache'
result = snapshot_download('m-a-p/$MODEL_NAME', cache_dir=cache_dir)
for f in os.listdir(result):
    src = os.path.join(result, f)
    dst = os.path.join('$MODEL_DIR', f)
    if os.path.isfile(src):
        shutil.copy2(src, dst)
print(f'Done in {time.time()-t0:.0f}s')
" 2>&1 | tail -5 | tee -a "$LOG"
    fi

    echo "$OUT_KEY: START $(date)" | tee -a "$LOG"
    python3 -m lm_eval \
      --model hf \
      --model_args pretrained=$MODEL_DIR,trust_remote_code=True \
      --tasks lambada_openai,arc_easy \
      --device cuda:0 \
      --batch_size auto \
      --log_samples \
      --output_path "$OUTDIR/${OUT_KEY}/" 2>&1 | tail -10 | tee -a "$LOG"
    echo "$OUT_KEY: DONE $(date)" | tee -a "$LOG"
    echo "" | tee -a "$LOG"
  done
done

# Priority 2B: RetNet and HGRN2 lambada eval (existing models, missing per-sample lambada data)
for arch_name in RetNet HGRN2; do
  for ratio in pure hybrid-24-1 hybrid-12-1 hybrid-6-1 hybrid-3-1; do
    OUT_KEY="${arch_name}_${ratio}_lambda_only"

    # Skip h3-1 for RetNet/HGRN2 (already done in Priority 1)
    if [ "$ratio" = "hybrid-3-1" ]; then
      continue
    fi

    # Skip if already evaluated
    if find "$OUTDIR/${OUT_KEY}" -name "samples_lambada_openai_*.jsonl" 2>/dev/null | grep -q .; then
      echo "$OUT_KEY: already done, skipping" | tee -a "$LOG"
      continue
    fi

    # Determine model path
    if [ "$arch_name" = "RetNet" ] && [ "$ratio" = "pure" ]; then
      MODEL_DIR="$MODELS/340M-20B-RetNet-pure"
    elif [ "$arch_name" = "HGRN2" ] && [ "$ratio" = "pure" ]; then
      MODEL_DIR="$MODELS/340M-20B-HGRN2-pure-baseline"
    else
      MODEL_DIR="$MODELS/340M-20B-${arch_name}-${ratio}"
    fi

    if [ ! -d "$MODEL_DIR" ]; then
      echo "$OUT_KEY: MODEL NOT FOUND at $MODEL_DIR, skipping" | tee -a "$LOG"
      continue
    fi

    echo "$OUT_KEY: START $(date)" | tee -a "$LOG"
    python3 -m lm_eval \
      --model hf \
      --model_args pretrained=$MODEL_DIR,trust_remote_code=True \
      --tasks lambada_openai \
      --device cuda:0 \
      --batch_size auto \
      --log_samples \
      --output_path "$OUTDIR/${OUT_KEY}/" 2>&1 | tail -10 | tee -a "$LOG"
    echo "$OUT_KEY: DONE $(date)" | tee -a "$LOG"
    echo "" | tee -a "$LOG"
  done
done

echo "=== Priority 2 ALL DONE $(date) ===" | tee -a "$LOG"
