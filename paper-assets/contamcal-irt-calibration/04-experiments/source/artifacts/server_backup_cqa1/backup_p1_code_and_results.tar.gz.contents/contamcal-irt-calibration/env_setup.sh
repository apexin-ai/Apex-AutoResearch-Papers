#!/bin/bash
source /etc/network_turbo 2>/dev/null || true
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt
export HF_HOME=/root/autodl-tmp/.hf_cache
export HF_HUB_DISABLE_XET=1
export TOKENIZERS_PARALLELISM=false
export MODEL_DIR=/root/autodl-tmp/models
export DATA_DIR=/root/autodl-tmp/.hf_cache
export OUTPUT_DIR=/root/contamcal-irt-calibration/outputs
