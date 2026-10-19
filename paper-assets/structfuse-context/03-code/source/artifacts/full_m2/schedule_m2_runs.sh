#!/bin/bash
# ============================================================================
# schedule_m2_runs.sh — 在双卡上调度 9 runs (3 strategies × 3 seeds)
#
# 分配策略 (双卡并行，卡内串行，按预估耗时均衡):
#   GPU 0 (5 runs): random_42 → embedding_42 → dataflow_42 → random_43 → embedding_43
#   GPU 1 (4 runs): random_44 → embedding_44 → dataflow_44 → dataflow_43
#
# 逻辑: seed=42 和 seed=44 各 3 runs 分别绑卡，seed=43 拆分到两卡平衡负载。
#        random 最快 (无额外计算)，dataflow 最慢 → GPU1 少一个 run 来平衡。
#
# Usage:
#   nohup bash schedule_m2_runs.sh > /root/autodl-tmp/structfuse/full_m2_schedule.log 2>&1 &
#
# 监控:
#   tail -f /root/autodl-tmp/structfuse/full_m2_schedule.log
#   ls /root/autodl-tmp/structfuse/full_m2_outputs/*/train.log
# ============================================================================

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
RUNNER="${SCRIPT_DIR}/run_full_m2_training.sh"
DATA_BUILDER="${SCRIPT_DIR}/build_full_m2_data.sh"
SCHEDULE_LOG="/root/autodl-tmp/structfuse/full_m2_schedule.log"
DATA_DIR="/root/autodl-tmp/structfuse/full_m2_training_data"

if [ ! -f "$RUNNER" ]; then
    echo "ERROR: runner script not found: $RUNNER"
    exit 1
fi

# ── Phase 0: Data Preparation ───────────────────────────────────────
echo "============================================"
echo " Phase 0: Data Preparation"
echo " Start: $(date '+%Y-%m-%d %H:%M:%S')"
echo "============================================"

if [ -f "${DATA_DIR}/train_random_s42.jsonl" ] && \
   [ -f "${DATA_DIR}/train_random_s43.jsonl" ] && \
   [ -f "${DATA_DIR}/train_random_s44.jsonl" ]; then
    echo "Training data already exists in ${DATA_DIR}, skipping build."
else
    if [ ! -f "$DATA_BUILDER" ]; then
        echo "ERROR: data builder not found: $DATA_BUILDER"
        exit 1
    fi
    bash "$DATA_BUILDER"
    echo "Data preparation complete."
fi

echo ""
echo "============================================"
echo " Phase 1: M2 Full Training Schedule"
echo " Start: $(date '+%Y-%m-%d %H:%M:%S')"
echo " 9 runs = 3 strategies × 3 seeds"
echo " GPU 0: 5 runs | GPU 1: 4 runs"
echo "============================================"

# ── GPU 0: 5 runs ────────────────────────────────────────────────────
run_gpu0() {
    local runs=(
        "random 42"
        "embedding_distance 42"
        "dataflow_aware 42"
        "random 43"
        "embedding_distance 43"
    )
    for run in "${runs[@]}"; do
        read -r strategy seed <<< "$run"
        echo "[GPU0][$(date '+%Y-%m-%d %H:%M:%S')] START ${strategy}_s${seed}"
        bash "$RUNNER" "$strategy" "$seed" 0
        echo "[GPU0][$(date '+%Y-%m-%d %H:%M:%S')] DONE  ${strategy}_s${seed}"
        echo ""
    done
    echo "[GPU0][$(date '+%Y-%m-%d %H:%M:%S')] ALL DONE"
}

# ── GPU 1: 4 runs ────────────────────────────────────────────────────
run_gpu1() {
    local runs=(
        "random 44"
        "embedding_distance 44"
        "dataflow_aware 44"
        "dataflow_aware 43"
    )
    for run in "${runs[@]}"; do
        read -r strategy seed <<< "$run"
        echo "[GPU1][$(date '+%Y-%m-%d %H:%M:%S')] START ${strategy}_s${seed}"
        bash "$RUNNER" "$strategy" "$seed" 1
        echo "[GPU1][$(date '+%Y-%m-%d %H:%M:%S')] DONE  ${strategy}_s${seed}"
        echo ""
    done
    echo "[GPU1][$(date '+%Y-%m-%d %H:%M:%S')] ALL DONE"
}

# ── 双卡并行启动 ─────────────────────────────────────────────────────
run_gpu0 &
PID_GPU0=$!

run_gpu1 &
PID_GPU1=$!

echo "Launched GPU0 (PID=$PID_GPU0) and GPU1 (PID=$PID_GPU1)"
echo "Waiting for both to complete..."

FAIL=0
wait $PID_GPU0 || FAIL=1
wait $PID_GPU1 || FAIL=1

echo ""
echo "============================================"
if [ $FAIL -eq 0 ]; then
    echo " ALL 9 RUNS COMPLETED SUCCESSFULLY"
else
    echo " SOME RUNS FAILED — check individual logs"
fi
echo " End: $(date '+%Y-%m-%d %H:%M:%S')"
echo "============================================"

exit $FAIL
