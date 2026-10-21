#!/bin/bash
set -eo pipefail
source /etc/network_turbo
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
export HF_HOME=/root/autodl-tmp/.hf_cache
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt

OUTDIR=/root/entrainment_gated_ft/results/exp005_zoo_expansion
LOG=${OUTDIR}/priority1_v2.log
MODELS=/root/entrainment_gated_ft/models

echo "=== Priority 1 v2 START $(date) ===" | tee "${LOG}"

# Phase A: Download 3 new arch models (without HF_HUB_DISABLE_XET for faster xet downloads)
for arch in GLA DeltaNet HGRN; do
  MODEL_NAME="340M-20B-${arch}-hybrid-3-1"
  MODEL_DIR="${MODELS}/${MODEL_NAME}"
  if [ -f "${MODEL_DIR}/model.safetensors" ]; then
    echo "${MODEL_NAME} already exists" | tee -a "${LOG}"
  else
    echo "Downloading ${MODEL_NAME} (xet enabled)..." | tee -a "${LOG}"
    rm -rf "${MODEL_DIR}/.cache" 2>/dev/null || true
    python3 -c "
from huggingface_hub import snapshot_download
import time
t0 = time.time()
snapshot_download('m-a-p/${MODEL_NAME}', local_dir='${MODEL_DIR}')
print(f'Done in {time.time()-t0:.0f}s')
" 2>&1 | tee -a "${LOG}"
  fi
done

echo "" | tee -a "${LOG}"
echo "=== Downloads complete, starting evals $(date) ===" | tee -a "${LOG}"

# Phase B: Evaluate 5 models on lambada_openai + arc_easy
export HF_HUB_DISABLE_XET=1
declare -A EVAL_MODELS
EVAL_MODELS[RetNet_h3-1]="${MODELS}/340M-20B-RetNet-hybrid-3-1"
EVAL_MODELS[HGRN2_h3-1]="${MODELS}/340M-20B-HGRN2-hybrid-3-1"
EVAL_MODELS[GLA_h3-1]="${MODELS}/340M-20B-GLA-hybrid-3-1"
EVAL_MODELS[DeltaNet_h3-1]="${MODELS}/340M-20B-DeltaNet-hybrid-3-1"
EVAL_MODELS[HGRN_h3-1]="${MODELS}/340M-20B-HGRN-hybrid-3-1"

for key in RetNet_h3-1 HGRN2_h3-1 GLA_h3-1 DeltaNet_h3-1 HGRN_h3-1; do
  MODEL_PATH="${EVAL_MODELS[${key}]}"
  echo "" | tee -a "${LOG}"
  echo "=== Evaluating ${key} START $(date) ===" | tee -a "${LOG}"
  python3 -m lm_eval \
    --model hf \
    --model_args pretrained=${MODEL_PATH},trust_remote_code=True \
    --tasks lambada_openai,arc_easy \
    --device cuda:0 \
    --batch_size auto \
    --log_samples \
    --output_path "${OUTDIR}/${key}" 2>&1 | tee -a "${LOG}"
  echo "=== ${key} DONE $(date) ===" | tee -a "${LOG}"
done

echo "" | tee -a "${LOG}"
echo "=== Priority 1 v2 ALL DONE $(date) ===" | tee -a "${LOG}"
