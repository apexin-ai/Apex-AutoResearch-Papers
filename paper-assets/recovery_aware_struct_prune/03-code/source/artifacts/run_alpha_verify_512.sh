#!/bin/bash
# α verification with calibration=512 (matching westb original)
# Only α=0.0 and α=4.0, GSM8K N=500 eval, dual GPU parallel
#
# Phase 0: Recompute importance + CKA scores with n_samples=512
# Phase 1: Prune α=0.0 and α=4.0 (parallel on 2 GPUs)
# Phase 2: Eval GSM8K N=500 (parallel on 2 GPUs)

set -euo pipefail

source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
source /etc/network_turbo 2>/dev/null || true
export HF_HOME=/root/autodl-tmp/.hf_cache
export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
export HF_HUB_DISABLE_XET=1

cd /root/recovery_aware_struct_prune

MODEL_PATH="/root/autodl-tmp/models/DeepSeek-R1-Distill-Qwen-7B"
OUTPUT_BASE="/root/autodl-tmp/recovery_aware_struct_prune/alpha_verify_512"
RESULT_DIR="results/alpha_verify_512"
SPARSITY=0.20
EVAL_SAMPLES=500

mkdir -p "$OUTPUT_BASE" "$RESULT_DIR"

echo "=========================================="
echo "Alpha Verification (calibration=512)"
echo "  Alphas: 0.0, 4.0"
echo "  Sparsity: ${SPARSITY}"
echo "  Calibration: 512 samples"
echo "  Eval: GSM8K N=${EVAL_SAMPLES}"
echo "  Start: $(date)"
echo "=========================================="

# === Phase 0: Compute importance + CKA with n_samples=512 ===
IMPORTANCE_512="results/importance_scores_512.pt"
CKA_512="results/cka_scores_512.pt"

if [ ! -f "$IMPORTANCE_512" ]; then
    echo "[Phase 0] Computing importance scores (n_samples=512)..."
    CUDA_VISIBLE_DEVICES=0 python src/importance_score.py \
        --model_path "$MODEL_PATH" \
        --output_path "$IMPORTANCE_512" \
        --n_samples 512 \
        --dtype bfloat16
    echo "[DONE] Importance scores: $(date)"
else
    echo "[SKIP] importance_scores_512.pt exists"
fi

if [ ! -f "$CKA_512" ]; then
    echo "[Phase 0] Computing CKA scores (n_samples=512)..."
    CUDA_VISIBLE_DEVICES=0 python src/cka_overlap.py \
        --model_path "$MODEL_PATH" \
        --output_path "$CKA_512" \
        --n_samples 512 \
        --dtype bfloat16
    echo "[DONE] CKA scores: $(date)"
else
    echo "[SKIP] cka_scores_512.pt exists"
fi

# === Phase 1: Prune α=0.0 and α=4.0 in parallel ===
echo ""
echo "=== Phase 1: Pruning ==="

PRUNE_0="${OUTPUT_BASE}/alpha_0.0"
PRUNE_4="${OUTPUT_BASE}/alpha_4.0"

if [ ! -f "${PRUNE_0}/config.json" ]; then
    echo "[PRUNE] GPU0 | alpha=0.0 | $(date '+%H:%M:%S')"
    CUDA_VISIBLE_DEVICES=0 python src/prune.py \
        --model_path "$MODEL_PATH" \
        --importance_path "$IMPORTANCE_512" \
        --cka_path "$CKA_512" \
        --mode rasp \
        --sparsity $SPARSITY \
        --alpha 0.0 \
        --output_path "$PRUNE_0" &
    PID_P0=$!
else
    echo "[SKIP] alpha=0.0 prune exists"
    PID_P0=""
fi

if [ ! -f "${PRUNE_4}/config.json" ]; then
    echo "[PRUNE] GPU1 | alpha=4.0 | $(date '+%H:%M:%S')"
    CUDA_VISIBLE_DEVICES=1 python src/prune.py \
        --model_path "$MODEL_PATH" \
        --importance_path "$IMPORTANCE_512" \
        --cka_path "$CKA_512" \
        --mode rasp \
        --sparsity $SPARSITY \
        --alpha 4.0 \
        --output_path "$PRUNE_4" &
    PID_P1=$!
else
    echo "[SKIP] alpha=4.0 prune exists"
    PID_P1=""
fi

[ -n "${PID_P0:-}" ] && { wait $PID_P0 || { echo "GPU0 prune FAILED"; exit 1; }; }
[ -n "${PID_P1:-}" ] && { wait $PID_P1 || { echo "GPU1 prune FAILED"; exit 1; }; }
echo "Pruning complete: $(date)"

# === Phase 2: Eval GSM8K N=500 in parallel ===
echo ""
echo "=== Phase 2: Evaluation (N=${EVAL_SAMPLES}) ==="

EVAL_0="${RESULT_DIR}/eval_alpha_0.0.json"
EVAL_4="${RESULT_DIR}/eval_alpha_4.0.json"

echo "[EVAL] GPU0 | alpha=0.0 | $(date '+%H:%M:%S')"
CUDA_VISIBLE_DEVICES=0 python src/eval_gsm8k.py \
    --model_path "$PRUNE_0" \
    --output_path "$EVAL_0" \
    --max_samples $EVAL_SAMPLES \
    --max_new_tokens 4096 \
    --dtype bfloat16 &
PID_E0=$!

echo "[EVAL] GPU1 | alpha=4.0 | $(date '+%H:%M:%S')"
CUDA_VISIBLE_DEVICES=1 python src/eval_gsm8k.py \
    --model_path "$PRUNE_4" \
    --output_path "$EVAL_4" \
    --max_samples $EVAL_SAMPLES \
    --max_new_tokens 4096 \
    --dtype bfloat16 &
PID_E1=$!

wait $PID_E0 || { echo "GPU0 eval FAILED"; exit 1; }
wait $PID_E1 || { echo "GPU1 eval FAILED"; exit 1; }
echo "Evaluation complete: $(date)"

# === Summary ===
echo ""
echo "=========================================="
echo "Verification Results (calibration=512)"
echo "=========================================="

python3 -c "
import json, os

result_dir = '${RESULT_DIR}'
print(f'{\"α\":>5} | {\"Accuracy\":>10} | {\"Correct\":>10} | {\"EOS Rate\":>10}')
print('-' * 50)
for alpha in [0.0, 4.0]:
    path = os.path.join(result_dir, f'eval_alpha_{alpha}.json')
    if not os.path.exists(path):
        print(f'{alpha:>5.1f} | MISSING')
        continue
    with open(path) as f:
        d = json.load(f)
    acc = d['accuracy']
    nc = d['n_correct']
    nt = d['n_total']
    eos = d['eos_stats']['eos_rate']
    print(f'{alpha:>5.1f} | {acc:>10.4f} | {nc:>4}/{nt:<5} | {eos:>10.2%}')

summary = {
    'calibration_samples': 512,
    'sparsity': ${SPARSITY},
    'eval_samples': ${EVAL_SAMPLES},
    'results': []
}
for alpha in [0.0, 4.0]:
    path = os.path.join(result_dir, f'eval_alpha_{alpha}.json')
    if os.path.exists(path):
        with open(path) as f:
            d = json.load(f)
        summary['results'].append({
            'alpha': alpha,
            'accuracy': d['accuracy'],
            'n_correct': d['n_correct'],
            'n_total': d['n_total'],
            'eos_rate': d['eos_stats']['eos_rate']
        })

out = os.path.join(result_dir, 'verify_512_summary.json')
with open(out, 'w') as f:
    json.dump(summary, f, indent=2)
print(f'\nSummary saved to {out}')
"

echo "=========================================="
echo "Complete: $(date)"
echo "=========================================="
