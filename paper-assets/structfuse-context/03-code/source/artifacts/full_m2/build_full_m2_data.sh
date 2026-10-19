#!/bin/bash
# ============================================================================
# build_full_m2_data.sh — 从 M1 extraction 构建 M2 训练数据
#
# 为 3 strategies × 3 seeds 生成训练/验证 JSONL 和 dataflow_graph.json
#
# Usage:
#   bash build_full_m2_data.sh
#
# 输入:
#   /root/autodl-tmp/structfuse/full_m1_data/  (migrate_m1_data.sh 迁移的 raw extraction)
#
# 输出:
#   /root/autodl-tmp/structfuse/full_m2_training_data/
#     train_{strategy}_s{seed}.jsonl   (strategy = random | embedding_distance | dataflow_aware)
#     val_{strategy}_s{seed}.jsonl
#     dataflow_graph.json
# ============================================================================

set -euo pipefail

PROJECT_ROOT="/root/structfuse"
BUILD_SCRIPT="${PROJECT_ROOT}/scripts/build_m1_training_data.py"
EXTRACTION_DIR="/root/autodl-tmp/structfuse/full_m1_data"
REPOS_DIR="/root/autodl-tmp/structfuse/full_m1_data/repos"
MODEL_PATH="/root/autodl-tmp/structfuse/models/Qwen/Qwen2.5-Coder-3B"
OUTPUT_DIR="/root/autodl-tmp/structfuse/full_m2_training_data"

SEEDS=(42 43 44)

# build_m1_training_data.py 输出名 → run_full_m2_training.sh 期望名
declare -A STRATEGY_MAP=(
    ["random"]="random"
    ["embedding"]="embedding_distance"
    ["dataflow"]="dataflow_aware"
)

echo "============================================"
echo " Build Full M2 Training Data"
echo " Start: $(date '+%Y-%m-%d %H:%M:%S')"
echo " Seeds: ${SEEDS[*]}"
echo " Output: ${OUTPUT_DIR}"
echo "============================================"

# 前置检查
for f in "$BUILD_SCRIPT" "$EXTRACTION_DIR" "$MODEL_PATH/config.json"; do
    if [ ! -e "$f" ]; then
        echo "ERROR: not found: $f"
        exit 1
    fi
done

if [ ! -d "$REPOS_DIR" ]; then
    echo "WARNING: repos dir not found: $REPOS_DIR"
    echo "  If repos are in a different location, update REPOS_DIR in this script."
    exit 1
fi

mkdir -p "$OUTPUT_DIR"

for seed in "${SEEDS[@]}"; do
    echo ""
    echo "── Seed ${seed} ───────────────────────────────"

    SEED_TMPDIR="${OUTPUT_DIR}/.tmp_s${seed}"
    mkdir -p "$SEED_TMPDIR"

    python -u "$BUILD_SCRIPT" \
        --extraction-dir "$EXTRACTION_DIR" \
        --repos-dir "$REPOS_DIR" \
        --output-dir "$SEED_TMPDIR" \
        --seed "$seed" \
        --model-path "$MODEL_PATH"

    # 重命名: train_embedding.jsonl → train_embedding_distance_s42.jsonl
    for src_name in "${!STRATEGY_MAP[@]}"; do
        dst_name="${STRATEGY_MAP[$src_name]}"
        mv "${SEED_TMPDIR}/train_${src_name}.jsonl" "${OUTPUT_DIR}/train_${dst_name}_s${seed}.jsonl"
    done

    # val.jsonl → val_{strategy}_s{seed}.jsonl (每个 strategy 相同 val，但用独立文件名保持一致)
    for dst_name in "${STRATEGY_MAP[@]}"; do
        cp "${SEED_TMPDIR}/val.jsonl" "${OUTPUT_DIR}/val_${dst_name}_s${seed}.jsonl"
    done

    # dataflow_graph.json 只需一份（seed 无关），首次拷贝
    if [ ! -f "${OUTPUT_DIR}/dataflow_graph.json" ]; then
        mv "${SEED_TMPDIR}/dataflow_graph.json" "${OUTPUT_DIR}/dataflow_graph.json"
    fi

    rm -rf "$SEED_TMPDIR"
    echo "  Seed ${seed} done."
done

echo ""
echo "============================================"
echo " Data build complete: $(date '+%Y-%m-%d %H:%M:%S')"
echo " Output files:"
ls -lh "${OUTPUT_DIR}"/*.jsonl "${OUTPUT_DIR}"/dataflow_graph.json 2>/dev/null
echo "============================================"
