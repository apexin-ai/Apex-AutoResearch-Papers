#!/bin/bash
set -e
cd /root/symb_invariant_consensus
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

export VLLM_USE_FLASHINFER_SAMPLER=0
export CUDA_VISIBLE_DEVICES=3

MODEL_DIR=/root/autodl-tmp/models/Qwen2.5-7B-Instruct
PORT=8003
RESULTS_DIR=results/exp004_qwen7b_rerun
mkdir -p $RESULTS_DIR

echo "=== [$(date)] exp-004-qwen7b-rerun ==="

# Download model using modelscope (better connectivity in China)
if [ ! -f "$MODEL_DIR/model-00001-of-00004.safetensors" ]; then
    echo "Downloading Qwen2.5-7B-Instruct via modelscope..."
    rm -rf $MODEL_DIR
    python -c "
from modelscope import snapshot_download
snapshot_download('Qwen/Qwen2.5-7B-Instruct', local_dir='$MODEL_DIR')
print('DOWNLOAD_DONE')
"
fi
echo "Model ready: $MODEL_DIR"
ls -la $MODEL_DIR/*.safetensors

# Start vLLM
echo "=== [$(date)] Starting vLLM ==="
python -m vllm.entrypoints.openai.api_server     --model $MODEL_DIR --port $PORT     --tensor-parallel-size 1 --gpu-memory-utilization 0.9     --max-model-len 8192 --enforce-eager     > /tmp/vllm_exp004_rerun.log 2>&1 &
VLLM_PID=$!
echo "vLLM PID: $VLLM_PID"

READY=0
for i in $(seq 1 300); do
    if curl -s http://localhost:$PORT/v1/models > /dev/null 2>&1; then
        echo "vLLM ready after ${i}s"
        READY=1
        break
    fi
    if ! kill -0 $VLLM_PID 2>/dev/null; then
        echo "ERROR: vLLM died"
        tail -30 /tmp/vllm_exp004_rerun.log
        exit 1
    fi
    sleep 1
done
if [ $READY -eq 0 ]; then
    echo "ERROR: vLLM timeout"
    kill $VLLM_PID 2>/dev/null || true
    exit 1
fi

# Run pipeline
echo "=== [$(date)] Running SICA D012 K=12 ==="
PYTHONUNBUFFERED=1 python -u run_full_mvp.py     --mode vllm --k 12 --temperature 0.7 --max-tokens 4096     --api-base http://localhost:$PORT/v1 --model auto --seed 42     --math-data data/empty.json     --pw-data data/proofwriter_d012.json     --folio-data data/folio_d012.json     --output $RESULTS_DIR/exp004_rerun_results.json     --save-intermediates     2>&1 | tee $RESULTS_DIR/exp004_rerun.log

EXIT_CODE=$?
kill $VLLM_PID 2>/dev/null || true
wait $VLLM_PID 2>/dev/null || true
echo "EXIT_CODE=$EXIT_CODE"
echo "EXP004_RERUN_DONE"
