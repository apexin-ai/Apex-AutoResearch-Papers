#!/bin/bash
set -e
cd .
source $CONDA_PREFIX/etc/profile.d/conda.sh && conda activate base
export PYTHONPATH=.:$PYTHONPATH
export VLLM_USE_V1=0

TARGET=57600
LOG_DIR=results/exp002

echo "$(date) — [GPU0-ACCEL] Creating placeholder internlm_math.jsonl to block chain"
python3 -c "
for i in range($TARGET):
    print('{\"_placeholder\": true}')
" > ${LOG_DIR}/internlm_math.jsonl
echo "$(date) — [GPU0-ACCEL] Placeholder created ($(wc -l < ${LOG_DIR}/internlm_math.jsonl) lines)"

echo "$(date) — [GPU0-ACCEL] Starting real InternLM MATH on GPU 0..."
CUDA_VISIBLE_DEVICES=0 python -m src.inference.run_experiment \
    --design ${LOG_DIR}/shard_internlm_math.csv \
    --benchmark math \
    --gpu-id 0 \
    --output ${LOG_DIR}/internlm_math_gpu0.jsonl \
    2>&1

REAL_LINES=$(wc -l < ${LOG_DIR}/internlm_math_gpu0.jsonl 2>/dev/null || echo 0)
echo "$(date) — [GPU0-ACCEL] Real run done: $REAL_LINES lines"

if [ "$REAL_LINES" -ge "$TARGET" ]; then
    mv ${LOG_DIR}/internlm_math_gpu0.jsonl ${LOG_DIR}/internlm_math.jsonl
    echo "$(date) — [GPU0-ACCEL] Swapped real data into internlm_math.jsonl"
else
    echo "$(date) — [GPU0-ACCEL] ERROR: only $REAL_LINES lines. Removing placeholder."
    rm -f ${LOG_DIR}/internlm_math.jsonl
fi
