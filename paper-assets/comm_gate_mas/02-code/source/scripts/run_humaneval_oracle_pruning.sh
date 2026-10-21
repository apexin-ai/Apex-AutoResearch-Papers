#!/bin/bash
# HumanEval oracle pruning: 5 seeds × paired baseline vs pruned on Qwen2.5-7B-Instruct.
# Requires: vLLM on bjb2 GPU 0, OPENAI_API_KEY for GPT-4o oracle calls.
set -euo pipefail

MODEL_PATH="/root/autodl-tmp/models/Qwen2.5-7B-Instruct"
PROJECT_DIR="/root/autodl-tmp/comm_gate_mas"
OUTPUT_BASE="${PROJECT_DIR}/outputs/humaneval_qwen_full/pruning"
VLLM_PORT=8000
SEEDS=(42 123 456 789 1024)
NUM_TASKS=164

: "${OPENAI_API_KEY:[REDACTED] must be set}"

source /etc/network_turbo 2>/dev/null || true
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt

source /root/miniconda3/etc/profile.d/conda.sh
conda activate base
export HF_HOME=/root/autodl-tmp/.hf_cache
export HF_HUB_DISABLE_XET=1

cd "${PROJECT_DIR}"
mkdir -p "${OUTPUT_BASE}"

exec > >(tee -a "${OUTPUT_BASE}/pruning_master.log") 2>&1
echo "=== HumanEval oracle pruning started at $(date) ==="

echo "Starting vLLM on port ${VLLM_PORT}..."
CUDA_VISIBLE_DEVICES=0 python -m vllm.entrypoints.openai.api_server \
    --model "${MODEL_PATH}" \
    --served-model-name "Qwen2.5-7B-Instruct" \
    --port "${VLLM_PORT}" \
    --max-model-len 4096 \
    --gpu-memory-utilization 0.85 &
VLLM_PID=$!
echo "vLLM PID: ${VLLM_PID}"

echo "Waiting for vLLM to become ready..."
for i in $(seq 1 60); do
    if curl -s "http://localhost:${VLLM_PORT}/v1/models" > /dev/null 2>&1; then
        echo "vLLM ready after ${i}s"
        break
    fi
    if ! kill -0 "${VLLM_PID}" 2>/dev/null; then
        echo "ERROR: vLLM process died during startup"
        exit 1
    fi
    sleep 5
done

if ! curl -s "http://localhost:${VLLM_PORT}/v1/models" > /dev/null 2>&1; then
    echo "ERROR: vLLM failed to start within 300s"
    kill "${VLLM_PID}" 2>/dev/null || true
    exit 1
fi

FAILED=0
for SEED in "${SEEDS[@]}"; do
    OUTPUT_FILE="${OUTPUT_BASE}/oracle_seed${SEED}.json"
    echo "=== Seed ${SEED} started at $(date) ==="
    if python src/humaneval_pruning.py \
        --mode oracle \
        --config configs/metagpt_qwen.yaml \
        --num-tasks "${NUM_TASKS}" \
        --seed "${SEED}" \
        --output "${OUTPUT_FILE}"; then
        echo "--- Seed ${SEED} done at $(date) ---"
        python3 -c "
import json
d = json.load(open('${OUTPUT_FILE}'))
s = d['statistics']
print(f\"  baseline={s['baseline_accuracy']:.4f} pruned={s['pruned_accuracy']:.4f} diff={s['accuracy_diff']:+.4f}\")
print(f\"  mcnemar_p={s['mcnemar']['p_value']:.4f} tost_p={s['tost_equivalence']['p_value']:.4f}\")
print(f\"  msg_reduction={s['messages']['reduction_pct']:.1f}%\")
"
    else
        echo "!!! Seed ${SEED} FAILED at $(date) !!!"
        FAILED=$((FAILED + 1))
    fi
done

echo "Stopping vLLM (PID ${VLLM_PID})..."
kill "${VLLM_PID}" 2>/dev/null || true
wait "${VLLM_PID}" 2>/dev/null || true

# Cross-seed aggregation
echo "=== Cross-seed aggregation ==="
python3 -c "
import json, glob, numpy as np
from scipy import stats

files = sorted(glob.glob('${OUTPUT_BASE}/oracle_seed*.json'))
print(f'Found {len(files)} seed result files')

deltas = []
for f in files:
    d = json.load(open(f))
    s = d['statistics']
    delta = s['accuracy_diff']
    deltas.append(delta)
    print(f\"  {f}: bl={s['baseline_accuracy']:.4f} pr={s['pruned_accuracy']:.4f} Δ={delta:+.4f}\")

if len(deltas) >= 2:
    mean_d = np.mean(deltas)
    sd_d = np.std(deltas, ddof=1)
    se_d = sd_d / np.sqrt(len(deltas))
    n = len(deltas)
    df = n - 1

    print(f'\nMean Δ = {mean_d:+.4f} ± {sd_d:.4f} (SD)')
    print(f'SE = {se_d:.4f}')

    # TOST (epsilon=1pp)
    eps = 0.01
    t_lo = (mean_d + eps) / se_d
    t_hi = (mean_d - eps) / se_d
    p_lo = 1 - stats.t.cdf(t_lo, df)
    p_hi = stats.t.cdf(t_hi, df)
    p_tost = max(p_lo, p_hi)
    print(f'TOST ε=1pp: p={p_tost:.4f} ({\"PASS\" if p_tost < 0.05 else \"FAIL\"})')

    # TOST (epsilon=5pp)
    eps5 = 0.05
    t_lo5 = (mean_d + eps5) / se_d
    t_hi5 = (mean_d - eps5) / se_d
    p_lo5 = 1 - stats.t.cdf(t_lo5, df)
    p_hi5 = stats.t.cdf(t_hi5, df)
    p_tost5 = max(p_lo5, p_hi5)
    print(f'TOST ε=5pp: p={p_tost5:.4f} ({\"PASS\" if p_tost5 < 0.05 else \"FAIL\"})')

    # Non-inferiority (delta=-3pp)
    t_ni = (mean_d + 0.03) / se_d
    p_ni = 1 - stats.t.cdf(t_ni, df)
    print(f'Non-inferiority δ=-3pp: p={p_ni:.4f} ({\"PASS\" if p_ni < 0.05 else \"FAIL\"})')

    # 90% CI
    ci = stats.t.interval(0.90, df, loc=mean_d, scale=se_d)
    print(f'90%% CI: [{ci[0]:+.4f}, {ci[1]:+.4f}]')
"

echo "=== All seeds complete at $(date). Failed: ${FAILED}/5 ==="
if [ "${FAILED}" -gt 0 ]; then
    exit 1
fi
echo "ALL_PRUNING_COMPLETE"
