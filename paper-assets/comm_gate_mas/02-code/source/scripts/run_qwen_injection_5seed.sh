#!/usr/bin/env bash
# Qwen ack injection 5-seed replication: seeds 42,123,456,789,1024
# GSM8K (300 tasks) + StratQA (250 tasks) per seed
# Usage: bash scripts/run_qwen_injection_5seed.sh [--force]
set -euo pipefail

source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

export HF_HUB_DISABLE_XET=1
export HF_HOME=/root/autodl-tmp/.hf_cache
export HF_DATASETS_OFFLINE=1
: "${OPENAI_API_KEY:[REDACTED] OPENAI_API_KEY not set. Source ~/.bashrc first.}"
export ORACLE_BASE_URL="http://47.94.22.126/v1"
export ORACLE_MODEL="openai/gpt-4o"

PROJECT_DIR="/root/autodl-tmp/comm_gate_mas"
cd "$PROJECT_DIR"

FORCE=0
if [[ "${1:-}" == "--force" ]]; then
    FORCE=1
fi

MODEL_PATH=""
for p in /root/autodl-tmp/models/Qwen2.5-7B-Instruct /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-7B-Instruct; do
    if [ -d "$p" ]; then MODEL_PATH="$p"; break; fi
done
if [ -z "$MODEL_PATH" ]; then echo "ERROR: Qwen model not found"; exit 1; fi

PORT=8000
SEEDS=(42 123 456 789 1024)
OUTDIR="outputs/qwen_injection_5seed"
GSM8K_CONFIG="configs/ack_injection_qwen_gsm8k.yaml"
STRATQA_CONFIG="configs/ack_injection_qwen_stratqa.yaml"

mkdir -p "$OUTDIR"

# --- Start vLLM ---
echo "=== Starting vLLM: model=$MODEL_PATH port=$PORT ==="
CUDA_VISIBLE_DEVICES=0 python3 -m vllm.entrypoints.openai.api_server \
    --model "$MODEL_PATH" \
    --served-model-name "/root/autodl-tmp/models/Qwen2.5-7B-Instruct" \
    --port "$PORT" \
    --gpu-memory-utilization 0.9 \
    --max-model-len 4096 \
    --trust-remote-code &
VLLM_PID=$!

echo "=== Waiting for vLLM (PID: $VLLM_PID) ==="
HEALTH_URL="http://127.0.0.1:${PORT}/health"
TIMEOUT_SECS=300
POLL_INTERVAL=5
ELAPSED=0

while [ "$ELAPSED" -lt "$TIMEOUT_SECS" ]; do
    if curl -sf "$HEALTH_URL" >/dev/null 2>&1; then
        echo "vLLM ready after ${ELAPSED}s"
        break
    fi
    if ! kill -0 "$VLLM_PID" 2>/dev/null; then
        echo "ERROR: vLLM process died"
        exit 1
    fi
    sleep "$POLL_INTERVAL"
    ELAPSED=$((ELAPSED + POLL_INTERVAL))
done

if ! curl -sf "$HEALTH_URL" >/dev/null 2>&1; then
    echo "ERROR: vLLM failed to start within ${TIMEOUT_SECS}s"
    kill "$VLLM_PID" 2>/dev/null || true
    exit 1
fi

# --- Run 5-seed loop ---
COMPLETED=0
SKIPPED=0

for SEED in "${SEEDS[@]}"; do
    # GSM8K
    GSM8K_OUT="$OUTDIR/gsm8k_seed_${SEED}.json"
    if [[ -f "$GSM8K_OUT" && "$FORCE" -eq 0 ]]; then
        echo "[skip] GSM8K seed=$SEED already exists: $GSM8K_OUT"
        SKIPPED=$((SKIPPED + 1))
    else
        echo "========================================="
        echo "[run] GSM8K seed=$SEED num_tasks=300"
        echo "========================================="
        python3 src/ack_injection.py \
            --config "$GSM8K_CONFIG" \
            --num-tasks 300 \
            --data-seed "$SEED" \
            --output "$GSM8K_OUT" \
            2>&1 | tee "$OUTDIR/gsm8k_seed_${SEED}.log"
        echo "[done] GSM8K seed=$SEED → $GSM8K_OUT"
        COMPLETED=$((COMPLETED + 1))
    fi

    # StratQA
    STRATQA_OUT="$OUTDIR/stratqa_seed_${SEED}.json"
    if [[ -f "$STRATQA_OUT" && "$FORCE" -eq 0 ]]; then
        echo "[skip] StratQA seed=$SEED already exists: $STRATQA_OUT"
        SKIPPED=$((SKIPPED + 1))
    else
        echo "========================================="
        echo "[run] StratQA seed=$SEED num_tasks=250"
        echo "========================================="
        python3 src/ack_injection.py \
            --config "$STRATQA_CONFIG" \
            --num-tasks 250 \
            --data-seed "$SEED" \
            --output "$STRATQA_OUT" \
            2>&1 | tee "$OUTDIR/stratqa_seed_${SEED}.log"
        echo "[done] StratQA seed=$SEED → $STRATQA_OUT"
        COMPLETED=$((COMPLETED + 1))
    fi
done

# --- Cleanup vLLM ---
echo "=== Stopping vLLM ==="
kill "$VLLM_PID" 2>/dev/null || true
wait "$VLLM_PID" 2>/dev/null || true

echo ""
echo "Finished: $COMPLETED completed, $SKIPPED skipped"

# --- Aggregate ---
echo "=== Aggregating results ==="
python3 -c "
import json, glob, numpy as np

for domain in ['gsm8k', 'stratqa']:
    files = sorted(glob.glob(f'$OUTDIR/{domain}_seed_*.json'))
    if not files:
        print(f'{domain}: no results found')
        continue
    print(f'\n--- {domain.upper()} ({len(files)} seeds) ---')
    deltas = []
    mcnemars = []
    for f in files:
        d = json.load(open(f))
        ctrl = d['control']['accuracy'] * 100
        inj = d['inject']['accuracy'] * 100
        delta = d['delta_pp']
        p = d.get('mcnemar_p')
        deltas.append(delta)
        if p is not None:
            mcnemars.append(p)
        print(f'  {f}: ctrl={ctrl:.1f}% inj={inj:.1f}% delta={delta:+.1f}pp p={p}')
    print(f'  Mean delta: {np.mean(deltas):+.2f}pp +/- {np.std(deltas, ddof=1):.2f}pp')
    print(f'  Range: [{min(deltas):+.1f}, {max(deltas):+.1f}]pp')
    if mcnemars:
        print(f'  McNemar p range: [{min(mcnemars):.4f}, {max(mcnemars):.4f}]')
"

echo "=== Qwen injection 5-seed replication finished ==="
