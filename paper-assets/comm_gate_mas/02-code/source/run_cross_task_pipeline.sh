#!/bin/bash
set -euo pipefail
LOG=/root/autodl-tmp/comm_gate_mas/pipeline.log
exec > >(tee -a "$LOG") 2>&1

cd /root/autodl-tmp/comm_gate_mas
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
export HF_HOME=/root/autodl-tmp/.hf_cache
export HF_DATASETS_OFFLINE=1

echo "=== Cross-task pipeline started at $(date) ==="

# --- Phase A: Wait for Llama nohup chain (StratQA → ARC) ---
LLAMA_CHAIN_PID=319949
if ps -p $LLAMA_CHAIN_PID > /dev/null 2>&1; then
    echo "[Phase A] Waiting for Llama chain (PID $LLAMA_CHAIN_PID) to finish..."
    while ps -p $LLAMA_CHAIN_PID > /dev/null 2>&1; do
        sleep 60
        echo "  Still running at $(date)"
    done
    echo "[Phase A] Llama chain finished at $(date)"
else
    echo "[Phase A] Llama chain (PID $LLAMA_CHAIN_PID) already done"
fi

# Verify Llama outputs
for f in outputs/llama_heuristic_stratqa.json outputs/llama_heuristic_arc.json; do
    if [ -f "$f" ]; then
        echo "[Phase A] OK: $f exists ($(wc -c < "$f") bytes)"
    else
        echo "[Phase A] WARNING: $f not found"
    fi
done

# --- Phase B: Switch to Qwen-7B ---
echo ""
echo "[Phase B] === Qwen-7B experiments ==="
echo "[Phase B] Stopping Llama vLLM on port 8001..."
pkill -f "vllm.*port.8001" || true
sleep 20

# Double-check port 8001 is free
for i in $(seq 1 12); do
    if ! curl -s http://localhost:8001/v1/models > /dev/null 2>&1; then
        echo "[Phase B] Port 8001 is free"
        break
    fi
    echo "[Phase B] Port 8001 still occupied, waiting..."
    sleep 10
done

echo "[Phase B] Starting Qwen2.5-7B vLLM on cuda:1 port 8001..."
CUDA_VISIBLE_DEVICES=1 python -m vllm.entrypoints.openai.api_server \
    --model /root/autodl-tmp/models/Qwen2.5-7B-Instruct \
    --served-model-name Qwen2.5-7B-Instruct \
    --port 8001 --max-model-len 4096 --gpu-memory-utilization 0.85 \
    --dtype auto > /tmp/vllm_qwen7b.log 2>&1 &
QWEN_PID=$!
echo "[Phase B] Qwen vLLM PID: $QWEN_PID"

# Wait for Qwen vLLM ready (up to 10 min)
READY=0
for i in $(seq 1 120); do
    if curl -s http://localhost:8001/v1/models > /dev/null 2>&1; then
        echo "[Phase B] Qwen vLLM ready after $((i*5))s"
        READY=1
        break
    fi
    if ! ps -p $QWEN_PID > /dev/null 2>&1; then
        echo "[Phase B] ERROR: Qwen vLLM died. Last 20 lines:"
        tail -20 /tmp/vllm_qwen7b.log
        exit 1
    fi
    sleep 5
done
if [ $READY -eq 0 ]; then
    echo "[Phase B] ERROR: Qwen vLLM failed to start in 600s"
    exit 1
fi

# Qwen StratQA
echo "[Phase B] Starting Qwen StratQA n=200..."
python3 src/pruning_validation.py --mode online_pruning \
    --config configs/stratqa_qwen_rr_port8001.yaml \
    --detection-mode heuristic --num-tasks 200 --data-seed 42 \
    --output outputs/qwen_heuristic_stratqa.json
echo "[Phase B] Qwen StratQA done at $(date)"

# Qwen ARC
echo "[Phase B] Starting Qwen ARC n=200..."
python3 src/pruning_validation.py --mode online_pruning \
    --config configs/arc_qwen_rr_port8001.yaml \
    --detection-mode heuristic --num-tasks 200 --data-seed 42 \
    --output outputs/qwen_heuristic_arc.json
echo "[Phase B] Qwen ARC done at $(date)"

# --- Phase C: Restore 72B ---
echo ""
echo "[Phase C] === Restore Qwen2.5-72B-AWQ ==="
echo "[Phase C] Stopping Qwen-7B vLLM..."
kill $QWEN_PID 2>/dev/null || pkill -f "vllm.*port.8001" || true
sleep 20

echo "[Phase C] Starting Qwen2.5-72B-Instruct-AWQ on cuda:1 port 8000..."
CUDA_VISIBLE_DEVICES=1 python -m vllm.entrypoints.openai.api_server \
    --model /root/autodl-tmp/models/Qwen2.5-72B-Instruct-AWQ \
    --served-model-name Qwen2.5-72B-Instruct-AWQ \
    --port 8000 --max-model-len 4096 --gpu-memory-utilization 0.90 \
    --dtype auto --quantization awq > /tmp/vllm_72b.log 2>&1 &
QWN72_PID=$!
echo "[Phase C] 72B vLLM PID: $QWN72_PID"

# Wait for 72B ready (up to 10 min)
READY=0
for i in $(seq 1 120); do
    if curl -s http://localhost:8000/v1/models > /dev/null 2>&1; then
        echo "[Phase C] 72B vLLM ready after $((i*5))s"
        READY=1
        break
    fi
    if ! ps -p $QWN72_PID > /dev/null 2>&1; then
        echo "[Phase C] ERROR: 72B vLLM died. Last 20 lines:"
        tail -20 /tmp/vllm_72b.log
        exit 1
    fi
    sleep 5
done
if [ $READY -eq 0 ]; then
    echo "[Phase C] WARNING: 72B vLLM not ready in 600s but process alive"
fi

echo ""
echo "=== Pipeline completed at $(date) ==="
echo "Outputs:"
ls -la outputs/llama_heuristic_stratqa.json outputs/llama_heuristic_arc.json \
      outputs/qwen_heuristic_stratqa.json outputs/qwen_heuristic_arc.json 2>/dev/null || true
echo "PIPELINE_DONE" > /root/autodl-tmp/comm_gate_mas/pipeline_sentinel.txt
