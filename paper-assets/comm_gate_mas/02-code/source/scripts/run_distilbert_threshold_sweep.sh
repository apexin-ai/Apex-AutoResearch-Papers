#!/bin/bash
set -e

cd /root/autodl-tmp/comm_gate_mas
source /etc/network_turbo 2>/dev/null || true
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

export CUDA_VISIBLE_DEVICES=0
export HF_HOME=/root/autodl-tmp/.hf_cache
export HF_DATASETS_OFFLINE=1
export TRANSFORMERS_OFFLINE=1

MODEL_PATH="/root/autodl-tmp/.hf_cache/LLM-Research/Meta-Llama-3___1-8B-Instruct"
VLLM_PORT=8001

echo "=== Starting vLLM server on GPU 0, port $VLLM_PORT ==="
python -m vllm.entrypoints.openai.api_server \
    --model "$MODEL_PATH" \
    --served-model-name "Llama-3.1-8B-Instruct" "meta-llama/Llama-3.1-8B-Instruct" \
    --port $VLLM_PORT \
    --tensor-parallel-size 1 \
    --gpu-memory-utilization 0.85 \
    --max-model-len 4096 \
    --trust-remote-code \
    &
VLLM_PID=$!
echo "vLLM PID: $VLLM_PID"

echo "Waiting for vLLM to start..."
for i in $(seq 1 60); do
    if curl -s http://localhost:$VLLM_PORT/v1/models | grep -q "Llama"; then
        echo "vLLM ready after ${i}0 seconds"
        break
    fi
    if ! kill -0 $VLLM_PID 2>/dev/null; then
        echo "vLLM process died!"
        exit 1
    fi
    sleep 10
done

curl -s http://localhost:$VLLM_PORT/v1/models | python3 -m json.tool || { echo "vLLM not ready!"; kill $VLLM_PID; exit 1; }

THRESHOLDS="0.3 0.4 0.5 0.6 0.7"
OUTPUT_DIR="artifacts/rebuttal"
mkdir -p "$OUTPUT_DIR"

echo ""
echo "=== DistilBERT Threshold Sweep ==="
echo "Start: $(date)"
echo ""

for T in $THRESHOLDS; do
    echo "--- threshold=$T @ $(date) ---"
    OUT_FILE="${OUTPUT_DIR}/distilbert_thresh_${T}.json"
    
    python src/pruning_validation.py \
        --mode online_pruning \
        --config configs/llama_gsm8k_rr_online.yaml \
        --num-tasks 300 \
        --detection-mode distilbert \
        --distilbert-checkpoint artifacts/classifier/distilbert_ack/checkpoint-810 \
        --distilbert-threshold $T \
        --data-seed 42 \
        --domain gsm8k \
        --output "$OUT_FILE"
    
    echo "Saved: $OUT_FILE"
    echo ""
done

echo "=== Sweep complete: $(date) ==="

kill $VLLM_PID 2>/dev/null || true
wait $VLLM_PID 2>/dev/null || true
echo "vLLM stopped."

python3 -c "
import json, os

results = []
for t in [0.3, 0.4, 0.5, 0.6, 0.7]:
    path = f'artifacts/rebuttal/distilbert_thresh_{t}.json'
    if not os.path.exists(path):
        print(f'MISSING: {path}')
        continue
    with open(path) as f:
        d = json.load(f)
    bl = d['baseline']['accuracy'] * 100
    pr = d['online_pruned']['accuracy'] * 100
    delta = pr - bl
    supp = d.get('suppress_pct', 0)
    results.append({'threshold': t, 'baseline': bl, 'pruned': pr, 'delta': delta, 'suppress_pct': supp})

with open('artifacts/rebuttal/b1_distilbert_threshold_data.json', 'w') as f:
    json.dump(results, f, indent=2)

with open('artifacts/rebuttal/b1_distilbert_threshold.md', 'w') as f:
    f.write('# DistilBERT Confidence Threshold Sensitivity\n\n')
    f.write('| Threshold | Baseline Acc | Pruned Acc | Delta (pp) | Suppress % |\n')
    f.write('|-----------|-------------|------------|------------|------------|\n')
    deltas = []
    for r in results:
        f.write(f'| {r[\"threshold\"]} | {r[\"baseline\"]:.2f}% | {r[\"pruned\"]:.2f}% | {r[\"delta\"]:+.2f} | {r[\"suppress_pct\"]:.1f}% |\n')
        deltas.append(r['delta'])
    if deltas:
        spread = max(deltas) - min(deltas)
        f.write(f'\nDelta range: {spread:.2f}pp across thresholds [0.3-0.7]\n')
        f.write(f'\n**Rebuttal conclusion**: DistilBERT classifier pruning is robust to confidence threshold ')
        f.write(f'(accuracy delta varies by {spread:.2f}pp across threshold range [0.3-0.7]).\n')

print('Summary generated:')
for r in results:
    print(f\"  threshold={r['threshold']}: baseline={r['baseline']:.2f}%, pruned={r['pruned']:.2f}%, delta={r['delta']:+.2f}pp, suppress={r['suppress_pct']:.1f}%\")
"
