source /etc/network_turbo 2>/dev/null || true
export HF_HOME=/root/autodl-tmp/.hf_cache
export HF_HUB_DISABLE_XET=1
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt
[ -f /root/miniconda3/etc/profile.d/conda.sh ] && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
