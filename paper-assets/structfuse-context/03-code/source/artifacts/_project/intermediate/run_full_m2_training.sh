#!/bin/bash
# ============================================================================
# run_full_m2_training.sh — 全量 M2 单次训练 wrapper
#
# Usage:
#   bash run_full_m2_training.sh <strategy> <seed> <gpu_id>
#
# Args:
#   strategy  — hard-negative 策略: random | embedding_distance | dataflow_aware
#   seed      — 随机种子: 42 | 43 | 44
#   gpu_id    — GPU 编号: 0 | 1
#
# Example:
#   bash run_full_m2_training.sh random 42 0
#   bash run_full_m2_training.sh embedding_distance 43 1
#
# 训练参数 (D013 确认):
#   batch_size=8, num_negatives=7, max_seq_length=2048, epochs=2
#   eval_steps=500, lr=2e-5, LoRA (r=16), gradient checkpointing
#
# 输出:
#   /root/autodl-tmp/structfuse/full_m2_outputs/${strategy}_s${seed}/
#
# 注意:
#   - train.py 当前无 --early-stopping-patience，如需 ES 须先给 train.py 加参数
#   - train.py 第 2 行硬编码了 CUDA_VISIBLE_DEVICES=4，本脚本通过环境变量覆盖
# ============================================================================

set -euo pipefail

# ── 参数解析 ─────────────────────────────────────────────────────────
STRATEGY="${1:?Usage: $0 <strategy> <seed> <gpu_id>}"
SEED="${2:?Usage: $0 <strategy> <seed> <gpu_id>}"
GPU_ID="${3:?Usage: $0 <strategy> <seed> <gpu_id>}"

VALID_STRATEGIES="random embedding_distance dataflow_aware"
if ! echo "$VALID_STRATEGIES" | grep -qw "$STRATEGY"; then
    echo "ERROR: strategy must be one of: $VALID_STRATEGIES"
    exit 1
fi

# ── 路径 ─────────────────────────────────────────────────────────────
PROJECT_ROOT="/root/structfuse"
MODEL_PATH="/root/autodl-tmp/structfuse/models/Qwen/Qwen2.5-Coder-3B"
DATA_DIR="/root/autodl-tmp/structfuse/full_m1_data"
OUTPUT_DIR="/root/autodl-tmp/structfuse/full_m2_outputs/${STRATEGY}_s${SEED}"
TRAIN_FILE="${DATA_DIR}/train_${STRATEGY}.jsonl"
VAL_FILE="${DATA_DIR}/val.jsonl"
DATAFLOW_GRAPH="${DATA_DIR}/dataflow_graph.json"
EMBEDDINGS_FILE="${DATA_DIR}/embeddings.npz"
LOG_FILE="${OUTPUT_DIR}/train.log"

# ── 环境变量 ──────────────────────────────────────────────────────────
export CUDA_VISIBLE_DEVICES="$GPU_ID"
export WANDB_MODE=offline
export TRANSFORMERS_OFFLINE=1
export HF_HUB_OFFLINE=1
export PYTHONUNBUFFERED=1

# ── 前置检查 ──────────────────────────────────────────────────────────
echo "=========================================="
echo " M2 Full Training"
echo " strategy=$STRATEGY  seed=$SEED  gpu=$GPU_ID"
echo " output=$OUTPUT_DIR"
echo "=========================================="

for f in "$TRAIN_FILE" "$VAL_FILE" "$MODEL_PATH/config.json"; do
    if [ ! -e "$f" ]; then
        echo "ERROR: required file not found: $f"
        exit 1
    fi
done

mkdir -p "$OUTPUT_DIR"

# ── 清理函数 ──────────────────────────────────────────────────────────
cleanup() {
    EXIT_CODE=$?
    if [ $EXIT_CODE -ne 0 ]; then
        echo "[$(date '+%Y-%m-%d %H:%M:%S')] FAILED: strategy=$STRATEGY seed=$SEED gpu=$GPU_ID exit_code=$EXIT_CODE" | tee -a "$LOG_FILE"
    else
        echo "[$(date '+%Y-%m-%d %H:%M:%S')] DONE: strategy=$STRATEGY seed=$SEED gpu=$GPU_ID" | tee -a "$LOG_FILE"
    fi
}
trap cleanup EXIT

# ── 构建训练命令 ──────────────────────────────────────────────────────
TRAIN_CMD=(
    python -u "${PROJECT_ROOT}/training/train.py"
    --model-name "$MODEL_PATH"
    --train-file "$TRAIN_FILE"
    --val-file "$VAL_FILE"
    --output-dir "$OUTPUT_DIR"
    --hard-negative-strategy "$STRATEGY"
    --seed "$SEED"
    --batch-size 8
    --num-negatives 7
    --max-seq-length 2048
    --num-epochs 2
    --learning-rate 2e-5
    --eval-steps 500
    --save-steps 1000
    --use-lora
    --gradient-checkpointing
    --wandb-project structfuse
    --wandb-run-name "full_m2_${STRATEGY}_s${SEED}"
)

# dataflow_aware 和 embedding_distance 需要额外文件
if [ "$STRATEGY" = "dataflow_aware" ] && [ -f "$DATAFLOW_GRAPH" ]; then
    TRAIN_CMD+=(--dataflow-graph-file "$DATAFLOW_GRAPH")
fi
if [ "$STRATEGY" = "embedding_distance" ] && [ -f "$EMBEDDINGS_FILE" ]; then
    TRAIN_CMD+=(--embeddings-file "$EMBEDDINGS_FILE")
fi

# ── 执行 ─────────────────────────────────────────────────────────────
echo "[$(date '+%Y-%m-%d %H:%M:%S')] START: ${TRAIN_CMD[*]}" | tee "$LOG_FILE"
"${TRAIN_CMD[@]}" 2>&1 | tee -a "$LOG_FILE"
