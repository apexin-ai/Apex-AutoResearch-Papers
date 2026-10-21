#!/bin/bash
export CUDA_VISIBLE_DEVICES=0,1  # D365: prevent GPU trespass to cuda:2/3
set -euo pipefail
cd /root/autodl-tmp/comm_gate_mas

echo "=== D364 Chain Start: $(date) ==="

# Kill existing vLLM
pkill -f "vllm.entrypoints" 2>/dev/null || true
sleep 3

# Start Qwen vLLM (tensor parallel on both GPUs)
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
python3 -m vllm.entrypoints.openai.api_server \
    --model /root/autodl-tmp/models/Qwen2.5-7B-Instruct \
    --port 8000 \
    --tensor-parallel-size 2 \
    --max-model-len 4096 \
    --gpu-memory-utilization 0.90 &
VLLM_PID=$!

echo "vLLM PID: $VLLM_PID, waiting for health..."
for i in $(seq 1 120); do
    curl -s http://127.0.0.1:8000/health > /dev/null 2>&1 && break
    kill -0 $VLLM_PID 2>/dev/null || { echo "FATAL: vLLM died"; exit 1; }
    sleep 5
done
curl -s http://127.0.0.1:8000/health > /dev/null 2>&1 || { echo "FATAL: vLLM timeout"; kill $VLLM_PID; exit 1; }
echo "vLLM ready: $(date)"

# === Phase 1: Qwen t=0.3 补 3 seeds ===
echo "=== Phase 1: Qwen t=0.3 seeds=123,456,789 ==="
mkdir -p outputs/qwen_heuristic_t03_multiseed
for SEED in 123 456 789; do
    OUT="outputs/qwen_heuristic_t03_multiseed/seed_${SEED}.json"
    [ -f "$OUT" ] && { echo "[skip] t03 seed=$SEED exists"; continue; }
    echo "[run] t=0.3 seed=$SEED N=200 th=150 — $(date)"
    python3 src/pruning_validation.py \
        --mode online_pruning \
        --config configs/qwen_gsm8k_heuristic_t03.yaml \
        --num-tasks 200 --data-seed $SEED \
        --detection-mode heuristic --char-threshold 150 \
        --output "$OUT" \
        2>&1 | tee "outputs/qwen_heuristic_t03_multiseed/seed_${SEED}.log"
    echo "[done] t=0.3 seed=$SEED — $(date)"
done

# === Phase 2: Qwen t=0.5 补 4 seeds ===
echo "=== Phase 2: Qwen t=0.5 seeds=123,456,789,1024 ==="
mkdir -p outputs/qwen_heuristic_t05_multiseed
for SEED in 123 456 789 1024; do
    OUT="outputs/qwen_heuristic_t05_multiseed/seed_${SEED}.json"
    [ -f "$OUT" ] && { echo "[skip] t05 seed=$SEED exists"; continue; }
    echo "[run] t=0.5 seed=$SEED N=200 th=150 — $(date)"
    python3 src/pruning_validation.py \
        --mode online_pruning \
        --config configs/qwen_gsm8k_heuristic_t05.yaml \
        --num-tasks 200 --data-seed $SEED \
        --detection-mode heuristic --char-threshold 150 \
        --output "$OUT" \
        2>&1 | tee "outputs/qwen_heuristic_t05_multiseed/seed_${SEED}.log"
    echo "[done] t=0.5 seed=$SEED — $(date)"
done

# === Phase 3: Three-Agent 3-seed ===
echo "=== Phase 3: Three-Agent Qwen GSM8K 3-seed ==="
bash scripts/run_three_agent_qwen_gsm8k_3seed.sh --force

# === Aggregation ===
echo "=== Aggregation ==="
python3 -c "
import json, glob, numpy as np, os
for label, pattern in [
    ('t0.3', 'outputs/qwen_heuristic_t03_multiseed/seed_*.json'),
    ('t0.5', 'outputs/qwen_heuristic_t05_multiseed/seed_*.json'),
    ('3agent', 'outputs/three_agent_qwen_gsm8k_3seed/seed_*.json')]:
    files = sorted(glob.glob(pattern))
    if not files:
        print(f'{label}: no files')
        continue
    deltas = []
    for f in files:
        d = json.load(open(f))
        bl = d.get('baseline', {}).get('accuracy', 0)
        pr = d.get('online_pruned', {}).get('accuracy', 0)
        if isinstance(bl, float) and bl <= 1: bl *= 100
        if isinstance(pr, float) and pr <= 1: pr *= 100
        delta = d.get('delta_pp', pr - bl)
        deltas.append(delta)
        sr = d.get('online_pruned', {}).get('suppress_pct', 0)
        print(f'  {label} {os.path.basename(f)}: bl={bl:.1f} pr={pr:.1f} d={delta:+.1f}pp sr={sr:.1f}%')
    if deltas:
        m = np.mean(deltas)
        s = np.std(deltas, ddof=1) if len(deltas)>1 else 0
        print(f'{label}: mean={m:+.2f}pp SD={s:.2f}pp n={len(deltas)}')
" 2>&1 || true

kill $VLLM_PID 2>/dev/null || true
echo "=== CHAIN_COMPLETE $(date) ==="
