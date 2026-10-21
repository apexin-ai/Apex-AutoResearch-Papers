#!/bin/bash
set -e
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/autodl-tmp/comm_gate_mas

export HF_HOME=/root/autodl-tmp/.hf_cache
export HF_DATASETS_OFFLINE=1

# Start Qwen vLLM on GPU 2, port 8000
echo "[$(date)] Starting Qwen vLLM on GPU 2, port 8000..."
CUDA_VISIBLE_DEVICES=2 python -m vllm.entrypoints.openai.api_server \
  --model /root/autodl-tmp/models/Qwen2.5-7B-Instruct \
  --served-model-name Qwen2.5-7B-Instruct \
  --port 8000 --host 0.0.0.0 \
  --max-model-len 8192 \
  --gpu-memory-utilization 0.9 > /tmp/vllm_qwen_3agent.log 2>&1 &
VLLM_PID=$!
echo "vLLM PID: $VLLM_PID"

# Wait for vLLM readiness
echo "Waiting for vLLM readiness..."
for i in $(seq 1 60); do
  if curl -s http://127.0.0.1:8000/v1/models | grep -q "Qwen"; then
    echo "vLLM ready after ${i} checks"
    break
  fi
  if [ $i -eq 60 ]; then
    echo "FATAL: vLLM not ready after 10 minutes"
    kill $VLLM_PID 2>/dev/null
    exit 1
  fi
  sleep 10
done

# Run trace collection for 3 seeds
SEEDS=(42 123 456)
BASE_CONFIG=configs/three_agent_qwen_gsm8k.yaml

mkdir -p outputs/three_agent_qwen_gsm8k_3seed

for seed in "${SEEDS[@]}"; do
  TRACE_DIR="outputs/three_agent_qwen_gsm8k_3seed/seed_${seed}"
  OUTPUT="${TRACE_DIR}/traces.jsonl"

  if [ -f "$OUTPUT" ]; then
    lines=$(wc -l < "$OUTPUT")
    if [ "$lines" -ge 100 ]; then
      echo "[3-agent] seed=$seed already done ($lines lines), skipping"
      continue
    fi
    echo "[3-agent] seed=$seed incomplete ($lines lines), re-running"
    rm -f "$OUTPUT"
  fi

  # Create temp config with modified seed and output path
  TEMP_CONFIG="/tmp/three_agent_seed_${seed}.yaml"
  cp "$BASE_CONFIG" "$TEMP_CONFIG"
  sed -i "s/seed: 42/seed: ${seed}/" "$TEMP_CONFIG"
  sed -i "s|trace_dir:.*|trace_dir: \"${TRACE_DIR}\"|" "$TEMP_CONFIG"
  sed -i "s|analysis_dir:.*|analysis_dir: \"${TRACE_DIR}\"|" "$TEMP_CONFIG"

  echo "[3-agent] Running seed=$seed at $(date)"
  python src/trace_collection.py \
    --config "$TEMP_CONFIG" \
    --output "$OUTPUT"
  echo "[3-agent] Finished seed=$seed at $(date)"
done

# Cleanup: kill vLLM
echo "Killing vLLM server..."
kill $VLLM_PID 2>/dev/null || true
wait $VLLM_PID 2>/dev/null || true

echo "=== 3-agent ALL DONE at $(date) ==="
