#!/bin/bash
set -euo pipefail

# eval_qwen7b_s42_cqa1.sh
# Re-evaluate Qwen-7B s42 with fixed evaluate.py (mc_suffix in assistant turn)
# Reference md5: 001a9bc23f808c47d25ef9eaeecb81f1 (37591 bytes)

source /etc/network_turbo 2>/dev/null || true
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
export HF_HOME=/root/autodl-tmp/.hf_cache
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt

cd /root/contamcal-irt-calibration/exp001

EVAL_MD5=$(md5sum evaluate.py | awk '{print $1}')
EVAL_SIZE=$(wc -c < evaluate.py)
if [ "$EVAL_MD5" != "001a9bc23f808c47d25ef9eaeecb81f1" ] || [ "$EVAL_SIZE" != "37591" ]; then
    echo "ERROR: evaluate.py md5/size mismatch! md5=$EVAL_MD5 size=$EVAL_SIZE"
    exit 1
fi
echo "[$(date)] evaluate.py verified: md5=$EVAL_MD5 size=$EVAL_SIZE"

BASE_MODEL="/root/autodl-tmp/models/Qwen2.5-7B/Qwen/Qwen2___5-7B"
CKPT_ROOT="/root/autodl-tmp/exp001/checkpoints"
OUT_ROOT="/root/autodl-tmp/exp001/eval_results_v2"

for DOSAGE in d000 d005 d025 d050 d100; do
    ADAPTER="${CKPT_ROOT}/Qwen2.5-7B_${DOSAGE}_s42/lora_adapter"
    OUT_DIR="${OUT_ROOT}/qwen7b_${DOSAGE}_s42_v2"

    if [ ! -d "$ADAPTER" ]; then
        echo "SKIP: adapter not found at $ADAPTER"
        continue
    fi

    ALPHA=$(grep -o '"lora_alpha": [0-9]*' "${ADAPTER}/adapter_config.json" | grep -o '[0-9]*')
    if [ "$ALPHA" != "32" ]; then
        echo "ERROR: ${DOSAGE} has lora_alpha=$ALPHA (expected 32), skipping"
        continue
    fi

    echo "[$(date)] Starting eval: ${DOSAGE} -> $OUT_DIR"
    CUDA_VISIBLE_DEVICES=0 python evaluate.py \
        --model-path "$BASE_MODEL" \
        --adapter-path "$ADAPTER" \
        --output-dir "$OUT_DIR" \
        --benchmarks mmlu arc_challenge \
        --mc-format aligned \
        --batch-size 8

    # Write eval_meta.json
    python3 -c "
import json, datetime
meta = {
    'evaluate_py_md5': '001a9bc23f808c47d25ef9eaeecb81f1',
    'server': 'cqa1-21977',
    'timestamp': datetime.datetime.now().isoformat(),
    'evaluate_py_size': 37591,
    'dosage': '${DOSAGE}',
    'seed': 42,
    'benchmarks': ['mmlu', 'arc_challenge'],
    'mc_format': 'aligned',
    'base_model': '${BASE_MODEL}',
    'adapter_path': '${ADAPTER}'
}
with open('${OUT_DIR}/eval_meta.json', 'w') as f:
    json.dump(meta, f, indent=2)
print(f'[eval_meta.json written to ${OUT_DIR}]')
"
    echo "[$(date)] Completed: ${DOSAGE}"
done

echo "[$(date)] All Qwen-7B s42 evals completed."
