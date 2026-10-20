#!/bin/bash
set -euo pipefail

# eval_qwen7b_s0_arc_cqa1.sh
# Evaluate Qwen-7B s0 (5 dosages) on ARC-Challenge 25-shot
# Reference evaluate.py md5: 001a9bc23f808c47d25ef9eaeecb81f1 (37591 bytes)

source /etc/network_turbo 2>/dev/null || true
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
export HF_HOME=/root/autodl-tmp/.hf_cache
export HF_DATASETS_OFFLINE=1
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt

cd /root/contamcal-irt-calibration/exp001

# C009: verify evaluate.py hash
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
    ADAPTER="${CKPT_ROOT}/Qwen2.5-7B_${DOSAGE}_s0/lora_adapter"
    OUT_DIR="${OUT_ROOT}/qwen7b_${DOSAGE}_s0"

    if [ ! -f "${ADAPTER}/adapter_config.json" ]; then
        echo "SKIP: adapter not ready at $ADAPTER"
        continue
    fi

    # C006: verify lora_alpha=32
    ALPHA=$(grep -o '"lora_alpha": [0-9]*' "${ADAPTER}/adapter_config.json" | grep -o '[0-9]*')
    if [ "$ALPHA" != "32" ]; then
        echo "ERROR: ${DOSAGE} has lora_alpha=$ALPHA (expected 32), skipping"
        continue
    fi

    # Skip if already done
    if [ -f "${OUT_DIR}/arc_challenge_results.json" ]; then
        echo "SKIP: ${DOSAGE} ARC already done at $OUT_DIR"
        continue
    fi

    echo "[$(date)] Starting ARC eval: ${DOSAGE} -> $OUT_DIR"
    # C004: explicit CUDA_VISIBLE_DEVICES
    CUDA_VISIBLE_DEVICES=0 python evaluate.py \
        --model-path "$BASE_MODEL" \
        --adapter-path "$ADAPTER" \
        --output-dir "$OUT_DIR" \
        --benchmarks arc_challenge \
        --mc-format aligned \
        --batch-size 8

    # Append ARC info to eval_meta if exists, or create new
    python3 -c "
import json, datetime, os
meta_path = '${OUT_DIR}/eval_meta.json'
if os.path.exists(meta_path):
    with open(meta_path) as f:
        meta = json.load(f)
    if 'arc_challenge' not in meta.get('benchmarks', []):
        meta['benchmarks'].append('arc_challenge')
        meta['arc_timestamp'] = datetime.datetime.now().isoformat()
else:
    meta = {
        'evaluate_py_md5': '001a9bc23f808c47d25ef9eaeecb81f1',
        'server': 'cqa1-21977',
        'timestamp': datetime.datetime.now().isoformat(),
        'evaluate_py_size': 37591,
        'dosage': '${DOSAGE}',
        'seed': 0,
        'benchmarks': ['arc_challenge'],
        'mc_format': 'aligned',
        'base_model': '${BASE_MODEL}',
        'adapter_path': '${ADAPTER}'
    }
with open(meta_path, 'w') as f:
    json.dump(meta, f, indent=2)
print(f'[eval_meta.json updated at ${OUT_DIR}]')
"
    echo "[$(date)] Completed ARC: ${DOSAGE}"
done

echo "[$(date)] All Qwen-7B s0 ARC evals completed."
