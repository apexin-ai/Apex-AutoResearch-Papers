#!/bin/bash
set -euo pipefail
source /etc/network_turbo 2>/dev/null || true
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt
export HF_HUB_DISABLE_XET=1
export HF_HOME=/root/autodl-tmp/.hf_cache
export HF_DATASETS_OFFLINE=1
export TRANSFORMERS_OFFLINE=1
source /root/miniconda3/etc/profile.d/conda.sh
conda activate base
